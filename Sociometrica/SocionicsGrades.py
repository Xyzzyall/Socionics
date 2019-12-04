from Socionics import Socionics
import numpy as np


class Grades:
    __h__ = np.empty(1)
    __refs__ = []

    def __init__(self, characteristics: dict):
        refs = characteristics.keys()
        self.__h__ = np.empty(len(refs))
        i = 0
        for name in refs:
            self.__h__[i] = characteristics[name]
            self.__refs__[i] = name
            i += 1

    def classify(self, relation: Socionics):
        n = len(self.__h__)
        k = np.empty(n)
        for i in range(n):
            k[i] = np.min(np.min(relation.__data__*relation.get(self.__refs__[i])))
        self.name(relation, k)
        k = k.transpose()
        return relation, np.matmul(k, self.__h__)

    def name(self, soc: Socionics, k):
        COMP_ERROR = 0.000001
        res = '{'
        for i in range(len(k)):
            if k > COMP_ERROR:
                res += ' ' + self.__refs__[i] + ':' + str(np.round(k*100)) + '%;'
        res += ' }'
        soc.name = res





