from old import Socionics as Soc
import numpy as np


class CompToFour(Soc.Psychotype):
    @staticmethod
    def get(name):
        mtx = Soc.Psychotype.get(name).__data__
        new_mtx = np.zeros((4, 4), dtype=np.int)
        k = 0
        for j in range(8):
            for i in range(4):
                if mtx[i, j] == 1:
                    if j == 0 or j == 3 or j == 4 or j == 7:
                        new_mtx[i, k] = -1
                    else:
                        new_mtx[i, k] = 1
                    k += 1

        res = CompToFour(new_mtx)
        res.name = name
        return res
