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


def balance(matrix: np.ndarray, u=True):
    n = len(matrix)
    d = matrix.copy()
    if u:
        for i in range(n):
            d[i, i] = 1

    def pred_sum(matrix, predicate):
        res = []
        for row in matrix:
            num = 0
            for elem in row:
                if predicate(elem):
                    num += elem
            res.append(num)
        return np.array(res).transpose()

    def is_subset(x: list, y: list):
        return set(y).issubset(set(x))

    def find_max(array):
        ind = 0
        mx = 0
        for i in range(len(array)):
            if array[i] > mx:
                mx = array[i]
                ind = i
        return ind

    def delete_rows(matrix, rows):
        res = []
        for i in range(len(matrix)):
            if not rows[i]:
                res.append(matrix[i])
        return np.array(res)

    a = d.copy()
    res = []
    n = np.array(list(range(n))).transpose()
    while len(a) > 0:
        s_list = pred_sum(a, lambda x: x > 0)
        i_star = find_max(s_list)
        pos_i_star_row = np.array([(1 if elem > 0 else 0) for elem in a[i_star]])
        s1 = np.matmul(a, pos_i_star_row.transpose())
        b = np.array([(1 if s1[i] == s_list[i] else 0) for i in range(len(s1))])
        #n1 = np.array([n, b])
        a = delete_rows(a, b)
        for i in range(len(b)):
            if b[i]:
                res.append(n[i])
        n = delete_rows(n, b)
    return res

