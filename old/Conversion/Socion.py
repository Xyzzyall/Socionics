from old import Socionics as Soc
import numpy as np


class Socion:
    @staticmethod
    def perm(type1, type2):
        a = Soc.Psychotype.get('DK').__data__
        b = Soc.Psychotype.get('Du').__data__
        c = Soc.Psychotype.get('Mk').__data__
        d = Soc.Psychotype.get('Gm').__data__
        res = np.zeros((8, 8), dtype=np.int)
        res2 = np.zeros((8, 8), dtype=np.int)
        arr = [-1, -1, 1, 1, 1, 1, 1, 1]
        arr2 = [1, 1, -1, -1, 1, 1, -1, 1]
        k = 0
        for i in range(8):
            res[i][k] = 1
            k += 1
        k = 0
        for i in range(8):
            res[i][k] = arr[i]
            k += 1
        k = 0
        for i in range(8):
            res2[i][k] = arr2[i]
            k += 1

        print(res)

        mult = np.zeros((8, 8), dtype=np.int)
        np.matmul(res, res2.transpose(), mult)
        print(mult)
