import Socionics as Soc
import numpy as np


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

        res = ConversionPsychotype(new_mtx)
        res.name = name
        return res
