import Socionics as Soc
import numpy as np
import math
from itertools import permutations


class ConversionPsychotype(Soc.Psychotype):
    @staticmethod
    def get(name):
        mtx = Soc.Psychotype.get(name).__data__
        new_mtx = np.zeros((4, 4), dtype=np.complex)
        for i in range(8):
            for j in range(4, 8):
                if mtx[i, j] == 1:
                    mtx[i, j-4] = 1
        for i in range(4):
            for j in range(4):
                new_mtx[i, j] = mtx[i, j]
        for i in range(4, 8):
            for j in range(4):
                if mtx[i, j] == 1:
                    new_mtx[i-4, j] = 1j
        for i in range(4):
            for j in range(4):
                if new_mtx[i, j] == 0:
                    new_mtx[i, j] = 2

        res = ConversionPsychotype(new_mtx)
        res.name = name
        return res


class ConversionRelation(Soc.Psychotype):
    @staticmethod
    def get(name):
        mtx = Soc.Relation.get(name).__data__
        new_mtx = np.zeros((4, 4), dtype=np.complex)
        for i in range(8):
            for j in range(4, 8):
                if mtx[i, j] == 1:
                    mtx[i, j-4] = 1
        for i in range(4):
            for j in range(4):
                new_mtx[i, j] = mtx[i, j]
        for i in range(4, 8):
            for j in range(4):
                if mtx[i, j] == 1:
                    new_mtx[i-4, j] = 1j

        res = ConversionRelation(new_mtx)
        res.name = name
        return res

    def exp_all_relations(self):
        pass


class ConversionPsychotype2(Soc.Psychotype):
    @staticmethod
    def get(name):
        mtx = Soc.Psychotype.get(name).__data__
        arr = [0j for i in range(8)]
        new_mtx = np.zeros((8, 8), dtype=np.complex)
        arr[0] = 1j
        arr[1] = 0 - 1j
        arr[2] = 1
        arr[3] = 1 + 1j
        arr[4] = 1 - 1j
        arr[5] = -1
        arr[6] = -1 + 1j
        arr[7] = -1 - 1j

        k = 0
        for i in range(8):
            for j in range(8):
                if mtx[i, j] == 1:
                    new_mtx[i, k] = arr[j]
                    k += 1

    @staticmethod
    def dr_get(name, arr):
        mtx = Soc.Psychotype.get(name).__data__
        new_mtx = np.zeros((8, 8), dtype=np.complex)

        k = 0
        for i in range(8):
            for j in range(8):
                if mtx[i, j] == 1:
                    new_mtx[i, k] = arr[j]
                    k += 1


        res = ConversionPsychotype(new_mtx)
        res.name = name
        return res


class ConversionPsychotype3(Soc.Psychotype):
    @staticmethod
    def get(name):
        mtx = Soc.Psychotype.get(name).__data__
        new_mtx = np.zeros((4, 4), dtype=np.int)

        for i in range(0, 5, 4):
            for j in range(0, 5, 4):

                if mtx[i][j] or mtx[i][j+1] or mtx[i][j+2] or mtx[i][j+3] or mtx[i+1][j] or mtx[i+1][j+1] or mtx[i+1][j+2] or mtx[i+1][j+3] == 1:
                    new_mtx[i//2][j//2] = 1
                else:
                    new_mtx[i//2][j//2] = 0

                if ((mtx[i][j] or mtx[i+1][j] or mtx[i+2][j] or mtx[i+3][j]) and (mtx[i][j+3] or mtx[i+1][j+3] or mtx[i+2][j+3] or mtx[i+3][j+3])) or ((mtx[i][j+1] or mtx[i+1][j+1] or mtx[i+2][j+1] or mtx[i+3][j+1]) and (mtx[i][j+2] or mtx[i+1][j+2] or mtx[i+2][j+2] or mtx[i+3][j+2])) == 1:
                    if mtx[i][j] or mtx[i][j+1] or mtx[i][j+2] or mtx[i][j+3] == 0:
                        new_mtx[math.ceil(i/ 2)][math.ceil((j + 1) / 2)] = 1
                else:
                    if mtx[i][j] or mtx[i+1][j] or mtx[i+2][j] or mtx[i+3][j] == 1:
                        new_mtx[math.ceil(i/ 2)][math.ceil((j + 1) / 2)] = 0
                    else:
                        new_mtx[math.ceil(i / 2)][math.ceil((j + 1) / 2)] = 1

                ind = [0, 0]
                v = 0
                for k in range(i, i + 4):
                    for m in range(j, j + 4):
                        if mtx[k][m] == 1:
                            ind[v] = m
                            v += 1
                if ind[0] > ind[1]:
                    new_mtx[math.ceil((i + 1) / 2)][math.ceil(j / 2)] = 1
                else:
                    new_mtx[math.ceil((i + 1) / 2)][math.ceil(j / 2)] = 0

        res = ConversionPsychotype(new_mtx)
        res.name = name
        return res