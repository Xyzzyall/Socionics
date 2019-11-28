import numpy as np


class Socionics:
    name = ''
    __data__ = np.empty((8, 8))

    def __init__(self, data):
        self.__data__ = np.array(data)

    @staticmethod
    def get_name(gr, i):
        pass

    @staticmethod
    def get_names():
        pass

    @staticmethod
    def get(name):
        pass

    def mult(self, other):
        res = Socionics(np.matmul(self.__data__, np.transpose(other.__data__)))
        res.name = self.name + '*' + other.name + "'"
        return res

    def __eq__(self, other):
        COMP_ERROR = 0.0000001
        if sum(sum(abs(self.__data__ - other.__data__))) < COMP_ERROR:
            return True
        else:
            return False

    def __str__(self):
        return self.__class__.__name__ + ' ' + self.name
