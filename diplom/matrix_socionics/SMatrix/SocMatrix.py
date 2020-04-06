import numpy as np
import diplom.matrix_socionics.SMatrix.Ptypes as Ptype


class SMatrix:
    name = ''
    __data__ = np.empty((4, 4))

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

    def mult(self, other):
        res = SMatrix(np.matmul(self.__data__, np.transpose(other.__data__)))
        res.name = self.name + '*' + other.name + "'"
        return res

    @staticmethod
    def comp_to_two(tup, i):
        psy = Ptype.Ptype.get_names()
        m = Ptype.Ptype.get(psy[tup]).__data__  # чтение исходной матрицы 4X4
        m = m[np.ix_(i, i)]  # применяет перестановку i одновременно на строки и столбцы

        mtx = np.zeros((2, 2), dtype=np.complex)
        change = [[0, 0, 0, 0], [0, 1, 1, 0], [1, 0, 0, 1], [-1, 0, 0, -1], [0, -1, -1, 0]]

        def cases(x):  # Функция замены содержимого матриц
            z = 0
            if x == change[1]:
                z = 1j
            elif x == change[2]:
                z = 1
            elif x == change[3]:
                z = -1
            elif x == change[4]:
                z = -1j
            return z

        u = [m[0][0], m[0][1], m[1][0], m[1][1]]
        o = [m[0][2], m[0][3], m[1][2], m[1][3]]
        p = [m[2][0], m[2][1], m[3][0], m[3][1]]
        l = [m[2][2], m[2][3], m[3][2], m[3][3]]

        t1 = u in change
        t2 = o in change
        t3 = p in change
        t4 = l in change

        if t1 and t2 and t3 and t4:
            mtx[0][0] = cases(u)
            mtx[0][1] = cases(o)
            mtx[1][0] = cases(p)
            mtx[1][1] = cases(l)
        return mtx
