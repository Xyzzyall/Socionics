import Socionics as Soc
import numpy as np
from itertools import permutations

class ComplexPerms:

    def perm(self):
        mtx = Soc.Psychotype.get('DK').__data__
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

        perm = permutations(arr)
        for p in perm:
            print(p)
            k = 0
            for i in range(8):
                for j in range(8):
                    if mtx[i, j] == 1:
                        new_mtx[i, k] = p[j]
                        k += 1