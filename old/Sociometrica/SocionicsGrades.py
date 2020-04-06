from old.Socionics import Socionics
import numpy as np


class Grades:
    __h__ = np.empty(1)
    __refs__ = []

    def __init__(self, characteristics: dict):
        refs = characteristics.keys()
        self.__h__ = np.empty(len(refs))
        self.__refs__ = ['' for i in range(len(refs))]
        i = 0
        for name in refs:
            self.__h__[i] = characteristics[name]
            self.__refs__[i] = name
            i += 1

    def classify(self, relation: Socionics):
        COMP_ERROR = 0.000001
        n = len(self.__h__)
        k = np.empty(n)
        for i in range(n):
            #TODO: спросить куренкова, почему это не работает
            #k[i] = np.trace(np.matmul(relation.get(self.__refs__[i]).__data__, relation.__data__.transpose()))
            #print(k[i])
            comp = relation.__data__*relation.get(self.__refs__[i]).__data__
            if np.min(sum(comp)) < COMP_ERROR:
                k[i] = 0
            else:
                k[i] = np.max(np.max(relation.__data__ * relation.get(self.__refs__[i]).__data__))
        self.name(relation, k)
        k = k.transpose()
        return relation, np.matmul(k, self.__h__)

    def name(self, soc: Socionics, k):
        COMP_ERROR = 0.000001
        res = ''
        for i in range(len(k)):
            if k[i] > COMP_ERROR:
                res += self.__refs__[i] + ':' + str(np.round(k[i]*100)) + '%;'
        soc.name = '{' + res + '}'

    def __str__(self):
        res = ''
        for i in range(len(self.__refs__)):
            res += self.__refs__[i] + ':' + str(self.__h__[i]) + '; '
        return res


