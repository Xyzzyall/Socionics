from threading import Thread
from diplom.database import DataBase
from diplom.analyzer.Groups import Groups
import old.Sociometrica.Balance as Balance
from diplom.socionics import Calculator
from diplom.database.DataBase import Request
from diplom.database.DataBase import RequestMany
import time

# todo: delete this
import numpy as np


class AnalyzerTask:
    collective = Groups
    grade = tuple

    def __init__(self, collective_size: int, grade: tuple):
        self.collective = Groups(collective_size)
        self.grade = grade


# todo: расспросить куренкова про функцию баланса. нужна быстрая функция без перестановок.

class Analyzer(Thread):
    task = AnalyzerTask
    database = DataBase
    soc_calc = Calculator

    _db_request_insert_grade = """
    INSERT INTO grade VALUES(
        null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    );
    SELECT COUNT(rowid) FROM grade
    """
    _db_request_insert_grade_stats = """
    INSERT INTO grade_stats VALUES(
        null, %s, %s, %s, %s, %s, %s, %s
    );
    SELECT COUNT(rowid) FROM grade_stats
    """
    _db_request_insert_many_groups = """
    INSERT INTO collective VALUES(
        null,?,?,?,?
    )
    """
    _db_request_max_groups_to_send = 500

    _db_request_update_grade_stats = """
    UPDATE grade_stats
    SET balanced0 = %s,
        balanced1 = %s,
        balanced2 = %s,
        balanced3 = %s,
        balanced_other = %s
    WHERE rowid == %s
    """

    def __init__(self, task: AnalyzerTask, name: str, database: DataBase):
        Thread.__init__(self, name=f'analyzer_{name}')
        self.task = task
        self.database = database
        self.soc_calc = Calculator()

    def run(self) -> None:
        # todo: delete this
        iterations = 0
        # out = open('test.txt', 'a')
        # grade_i = 0
        grade = self.task.grade

        # out.write("\n{'collective': " + str('dik') + ", 'grades': '" + str(grade) + "'")
        balanced_1b = 0
        balanced_2b = 0
        balanced_3b = 0
        balanced_other = 0
        non_balanced = 0

        # добавление начальных значений в бд, получение индексов в таблицах
        self.database.sign_up_thread()

        grade_rowid = []
        self.database.append_request(Request(
            Analyzer._db_request_insert_grade % grade,
            lambda rowid: grade_rowid.append(rowid[0])
        ))
        while len(grade_rowid) == 0:
            time.sleep(0.01)
        grade_rowid = grade_rowid[0][0]-1

        grade_stats_rowid = []
        self.database.append_request(Request(
            Analyzer._db_request_insert_grade_stats % (grade_rowid, self.task.collective.size, 0, 0, 0, 0, 0),
            lambda rowid: grade_stats_rowid.append(rowid)
        ))
        while len(grade_stats_rowid) == 0:
            time.sleep(0.01)
        grade_stats_rowid = grade_stats_rowid[0][0][0]-1
        print(f'Thread {self.name} appended to DB.')

        def group_balanced():
            for gr in self.task.collective:
                graded_collective = self.soc_calc.get_collective(gr, grade)
                inds = Balance.balance(np.array(graded_collective))
                balanced_coll = np.array(graded_collective)[np.ix_(inds, inds)]
                res = Balance.check_blocks(np.array(balanced_coll))
                yield res[0], res[1], inds, Calculator.get_psychotypes_from_vector(gr)

        groups_to_append = []

        for blocked, clasters, inds, group in group_balanced():
            if blocked:
                n = len(clasters)
                if n == 1:
                    balanced_1b += 1
                elif n == 2:
                    balanced_2b += 1
                elif n == 3:
                    balanced_3b += 1
                else:
                    balanced_other += 1
                groups_to_append.append((grade_stats_rowid, str([str(psycho) for psycho in group]), n, str(inds)))
                if len(groups_to_append) > Analyzer._db_request_max_groups_to_send:
                    self.database.append_request(RequestMany(
                        Analyzer._db_request_insert_many_groups,
                        groups_to_append
                    ))
                    groups_to_append = []
            else:
                non_balanced += 1
            iterations += 1
            # if iterations % 100 == 0:
            #     print(str(iterations) + ' is done.')

        if len(groups_to_append) > 0:
            self.database.append_request(RequestMany(
                Analyzer._db_request_insert_many_groups,
                groups_to_append
            ))

        self.database.append_request(Request(
            Analyzer._db_request_update_grade_stats % (
                non_balanced, balanced_1b, balanced_2b, balanced_3b, balanced_other, grade_stats_rowid
            )
        ))

        self.database.sign_out_thread()
        print(f'Thread {self.name} finished working. Done {iterations} iterations.')
        # balanced = balanced_1b + balanced_2b
        # out.write(", 'balanced':" + str(balanced) + ", '1 block':" + str(balanced_1b) + ", '2 blocks':" + \
        #        str(balanced_2b) + ", '3 blocks':" + str(balanced_3b) + ", 'non balanced':" + str(non_balanced) + "}")
        # grade_i += 1

        # print('Grade ' + str(grade_i) + ' analyzed.')
        # out.close()
        # print(
        #  'Analysis is done. Performed ' + str(iterations) + ' iterations, analyzed ' + str(grade_i + 1) + ' grades.')
        # todo: delete...
