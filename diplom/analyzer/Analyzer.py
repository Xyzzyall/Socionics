from threading import Thread
from diplom.database import DataBase
from diplom.analyzer.Groups import Groups
import old.Sociometrica.Balance as Balance
from diplom.socionics import Calculator

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

    def __init__(self, task: AnalyzerTask, name: str, database: DataBase):
        Thread.__init__(self, name=f'analyzer_{name}')
        self.task = task
        self.database = database
        self.soc_calc = Calculator()

    def run(self) -> None:
        # todo: delete this
        iterations = 0
        out = open('test.txt', 'a')
        grade_i = 0
        grade = self.task.grade

        out.write("\n{'collective': " + str('dik') + ", 'grades': '" + str(grade) + "'")
        balanced_1b = 0
        balanced_2b = 0
        balanced_3b = 0
        non_balanced = 0

        def group_balanced():
            f = open('debug.txt', 'w')
            for gr in self.task.collective:
                graded_collective = self.soc_calc.get_collective(gr, grade)
                inds = Balance.balance(np.array(graded_collective))
                balanced_coll = np.array(graded_collective)[np.ix_(inds, inds)]
                res = Balance.check_blocks(np.array(balanced_coll))
                f.write(str(graded_collective) + '\n' + str(balanced_coll) + '\n' + str(res) + '\n')
                yield res
            f.close()

        for blocked, clasters in group_balanced():
            if blocked:
                n = len(clasters)
                if n == 1:
                    balanced_1b += 1
                elif n == 2:
                    balanced_2b += 1
                elif n == 3:
                    balanced_3b += 1
                else:
                    non_balanced += 1
            else:
                non_balanced += 1
            iterations += 1
            if iterations % 100 == 0:
                print(str(iterations) + ' is done.')

        balanced = balanced_1b + balanced_2b
        out.write(", 'balanced':" + str(balanced) + ", '1 block':" + str(balanced_1b) + ", '2 blocks':" + \
                  str(balanced_2b) + ", '3 blocks':" + str(balanced_3b) + ", 'non balanced':" + str(non_balanced) + "}")
        grade_i += 1

        print('Grade ' + str(grade_i) + ' analyzed.')
        out.close()
        print(
            'Analysis is done. Performed ' + str(iterations) + ' iterations, analyzed ' + str(grade_i + 1) + ' grades.')
        # todo: delete...
