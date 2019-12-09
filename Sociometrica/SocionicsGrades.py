from Socionics import Socionics
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


def balance(M: np.ndarray, u: bool):
    def define_s_row(row, n):
        res = []
        for i in range(n):
            if row[i] > 0:
                res.append(i)
        return res

    def find_index_of_max_len(array):
        i = 0
        res = []
        max_len = 0
        max_index = 0
        for elem in array:
            if len(elem) > max_len:
                res = elem
                max_index = i
            i += 1
        return max_index, res

    def is_subset(a, b):
        for a_elem in a:
            if a_elem not in b:
                return False
        return True

    def g_function(s_rows, s_i_star):
        s_l = []
        s_l_rev = []
        for l in range(len(s_rows)):
            if is_subset(s_rows[l], s_i_star):
                s_l.append(l)
            else:
                s_l_rev.append(l)
        return s_l, s_l_rev

    D = M.copy()
    n = len(D)
    if u:
        for i in range(n):
            D[i, i] = 1
    for i in range(n):
        for j in range(n):
            D[i, j] = D[i, j] if D[i, j] > 0 else 0

    DD = D.copy()
    res = []
    while True:
        s_rows = [define_s_row(row, n) for row in DD]
        max_i, s_i_star = find_index_of_max_len(s_rows)
        s_l, s_l_rev = g_function(s_rows, s_i_star)
        DD = DD[s_l_rev, :]
        res.append(s_l)
        if len(DD) == 0:
            flat_res = []
            for array in res:
                for elem in array:
                    flat_res.append(elem)
            return flat_res


