from old import Good_4x4_Comp as Comp
import old.Socionics.Psychotypes as Soc
import numpy as np
from itertools import permutations


def perch(i, tup, number):
    pType = Soc.Psychotype.get_names()
    a = Comp.CompToFour.get(pType[tup]).__data__
    m = np.array(a)

    # m = m[i]
    # m = m.transpose()
    # m = m[j]
    # m = m.transpose()
    # m = m[h]
    # m = m.transpose()
    m = m[np.ix_(i, i)]

    mtxRes = np.zeros((2, 2), dtype=np.complex)
    change = [[0, 0, 0, 0], [0, 1, 1, 0], [1, 0, 0, 1], [-1, 0, 0, -1], [0, -1, -1, 0]]

    def cases(x):
        m = 0
        if x == change[1]:
            m = 1j
        elif x == change[2]:
            m = 1
        elif x == change[3]:
            m = -1
        elif x == change[4]:
            m = -1j
        return m

    u = [m[0][0], m[0][1], m[1][0], m[1][1]]
    o = [m[0][2], m[0][3], m[1][2], m[1][3]]
    p = [m[2][0], m[2][1], m[3][0], m[3][1]]
    l = [m[2][2], m[2][3], m[3][2], m[3][3]]

    t1 = u in change
    t2 = o in change
    t3 = p in change
    t4 = l in change

    if t1 and t2 and t3 and t4:
        mtxRes[0][0] = cases(u)
        mtxRes[0][1] = cases(o)
        mtxRes[1][0] = cases(p)
        mtxRes[1][1] = cases(l)
        print(number)
        print(mtxRes)
        print(i, '\n')
        #print(j)
        #print(h, '\n')
    return mtxRes


#perch([3, 1, 2, 0], 0)

k = 0
for i in permutations([0, 1, 2, 3]):
    k += 1
    i = list(i)
    #j = list(j)
    #h = list(h)
    perch(i, 0, k)
# For New Commit
