from Sociometrica import Sociometrica
from Sociometrica import Grades
import numpy as np


class BinaryRelations:
    __data__ = np.empty((1, 1))
    __names__ = []
    reference = None

    def __init__(self, data, names):
        self.__data__ = data
        self.__names__ = names.copy()

    @staticmethod
    def from_sociotypes(sociotypes: Sociometrica, grades: Grades):
        relations = sociotypes.get_raw_data()
        n = len(sociotypes)
        data = np.empty((n, n))
        for i in range(n):
            for j in range(n):
                relations[i][j], data[i, j] = grades.classify(relations[i][j])
        res = BinaryRelations(data, sociotypes.__names__)
        res.reference = sociotypes
        return res

    def __str__(self):
        names = [str(i + 1) + ': ' + self.__names__[i] for i in range(len(self.__names__))]
        psychos = [[str(i + 1)] + [str(elems) for elems in self.__data__[i]] for i in range(len(self.__names__))]

        res = ''
        for name in names:
            res += name + '; '
        res += '\n'

        psychos = [[str(i) for i in range(len(self.__names__) + 1)]] + psychos  # adding numeration
        for rows in psychos:
            for elems in rows:
                res += elems + '\t'
            res += '\n'
        res += '\nReference: {\n' + str(self.reference) + '\n}'
        return res




