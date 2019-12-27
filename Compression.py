import Socionics as Soc
import Conversion as Conv
import numpy as np
from itertools import permutations


arr = [0j for i in range(8)]
arr[0] = 1j
arr[1] = 0 - 1j
arr[2] = 1
arr[3] = 1 + 1j
arr[4] = 1 - 1j
arr[5] = -1
arr[6] = -1 + 1j
arr[7] = -1 - 1j

perm = permutations(arr)
e = 0
for p in perm:
    mtxA = Conv.ConversionPsychotype2.dr_get('Mk', arr).__data__
    mtxB = Conv.ConversionPsychotype2.dr_get('Gm', arr).__data__
    relDu = Conv.ConversionRelation.get('DU').__data__
    mtxC = Conv.ConversionPsychotype2.dr_get('DK', arr).__data__
    mtxD = Conv.ConversionPsychotype2.dr_get('Du', arr).__data__

    rel = np.zeros((8, 8), dtype=np.complex)
    rel2 = np.zeros((8, 8), dtype=np.complex)
    np.matmul(mtxA, mtxB, rel)
    np.matmul(mtxC, mtxD, rel2)

    #np.array_equal(rel, rel2):
    if sum(sum(abs(rel - rel2))) < 0.0000001:
        #print('True. Working')
        break
    else:
        #print('FUCK!!!!')
        e += 1
        if e == 20:
            break

a = [[1, 0, 0, 0],
     [0, 0, 0, 0],
     [1, 1, 0, 1],
     [0, 0, 0, 0]]
b = [[0, 0, 1, 0],
     [1, 0, 1, 0],
     [0, 1, 1, 1],
     [1, 0, 1, 0]]
c = [[0, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 1, 1, 1],
     [0, 0, 0, 0]]
d = [[1, 0, 0, 0],
     [1, 0, 1, 0],
     [1, 1, 0, 1],
     [1, 0, 1, 0]]
e = np.zeros((4, 4), dtype=np.int)
e2 = np.zeros((4, 4), dtype=np.int)
tb =[[b[j][i] for j in range(len(b))] for i in range(len(b[0]))]
td =[[d[j][i] for j in range(len(d))] for i in range(len(d[0]))]
np.matmul(a, tb, e)
np.matmul(c, td, e2)
print(e)
print(e2)

mtxA = Conv.ConversionPsychotype3.get('DK').__data__
mtxB = Conv.ConversionPsychotype3.get('Gs').__data__
tb =[[mtxB[j][i] for j in range(len(mtxB))] for i in range(len(mtxB[0]))]
np.matmul(mtxA, tb, e2)
print(e2)
print(mtxA)
mtxA = Conv.ConversionPsychotype2.dr_get('DK', arr).__data__
print(mtxA)