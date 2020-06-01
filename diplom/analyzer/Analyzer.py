from threading import Thread
from diplom.database import DataBase
from diplom.analyzer.Groups import Groups
import old.Sociometrica.Balance as Balance
from diplom.socionics import Calculator
from diplom.database.DataBase import Request
from diplom.database.DataBase import RequestMany
import time
import networkx as netx

# todo: delete this
import numpy as np


class AnalyzerTask:
    collective = Groups
    grade = tuple

    def __init__(self, collective_size: int, grade: tuple):
        self.collective = Groups(collective_size)
        self.grade = grade


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
        null, %s, %s
    );
    SELECT COUNT(rowid) FROM grade_stats
    """

    _db_request_insert_many_groups = """
    INSERT INTO collective VALUES(
        null,?,?, ?,?
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
        grade = self.task.grade

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
            Analyzer._db_request_insert_grade_stats % (grade_rowid, self.task.collective.size),
            lambda rowid: grade_stats_rowid.append(rowid)
        ))
        while len(grade_stats_rowid) == 0:
            time.sleep(0.01)
        grade_stats_rowid = grade_stats_rowid[0][0][0]-1
        print(f'Thread {self.name} appended to DB.')

        def group_analysis(group: tuple):
            signed_graph = self.soc_calc.matrix_to_graph(self.soc_calc.get_collective(group, self.task.grade))
            # there may be a little optimization...
            return self.soc_calc.balance(signed_graph), self.soc_calc.balance_length_weighted(signed_graph)

        groups_to_append = []

        for group in self.task.collective:
            balance, balance_len_weighted = group_analysis(group)

            groups_to_append.append((
                grade_stats_rowid,
                str([str(psycho) for psycho in group]),
                balance,
                balance_len_weighted
            ))

            if len(groups_to_append) > Analyzer._db_request_max_groups_to_send:
                self.database.append_request(RequestMany(
                    Analyzer._db_request_insert_many_groups,
                    groups_to_append
                ))
                groups_to_append = []

            iterations += 1

        if len(groups_to_append) > 0:
            self.database.append_request(RequestMany(
                Analyzer._db_request_insert_many_groups,
                groups_to_append
            ))

        # self.database.append_request(Request(
        #     Analyzer._db_request_update_grade_stats % (
        #         _, grade_stats_rowid
        #     )
        # ))

        self.database.sign_out_thread()
        print(f'Thread {self.name} finished working. Done {iterations} iterations.')

