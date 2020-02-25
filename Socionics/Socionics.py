import numpy as np


class Socionics:
    name = ''
    __data__ = np.empty((8, 8))

    def __init__(self, data):
        self.__data__ = np.array(data)
        self.name = 'unknown'

    @staticmethod
    def get_name(gr, i):
        pass

    @staticmethod
    def get_names():
        pass

    @staticmethod
    def get(name):
        pass

    @staticmethod
    def get_zero():
        pass

    def mult(self, other):
        res = Socionics(np.matmul(self.__data__, np.transpose(other.__data__)))
        res.name = self.name + '*' + other.name + "'"
        return res

    def decompose(self):
        """
            ВАЖНО: считается, что все компоненты матрицы данных ровно распределены по базисам социотипа/отношений
        :return:
            процент "содержания" каждого социотипа/отношения в объекте
        """
        res = {}
        for name in self.get_names():
            res[name] = max(max(self.get(name) * self.__data__))
        return res

    def __eq__(self, other):
        COMP_ERROR = 0.0000001
        if sum(sum(abs(self.__data__ - other.__data__))) < COMP_ERROR:
            return True
        else:
            return False

    def __str__(self):
        return self.__class__.__name__ + ' ' + self.name
