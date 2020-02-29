import Socionics as Soc
import Good_4x4_Comp as Comp
import numpy as np
from itertools import permutations


class CompToTwo(Soc.Psychotype):
    @staticmethod
    def get(name):
        mtxA = Comp.CompToFour.get(name).__data__
        a = np.array(mtxA)
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

        mas = []
        dic = {}
        try:
            ik = 0
            k = 0
            for i in permutations([0, 1, 2, 3]):
                mtx = a[[i]]
                mtx = mtx.transpose()
                for j in permutations([0, 1, 2, 3]):
                    b = mtx[[j]]
                    u = [b[0][0], b[0][1], b[1][0], b[1][1]]
                    o = [b[0][2], b[0][3], b[1][2], b[1][3]]
                    p = [b[2][0], b[2][1], b[3][0], b[3][1]]
                    l = [b[2][2], b[2][3], b[3][2], b[3][3]]
                    t1 = u in change
                    t2 = o in change
                    t3 = p in change
                    t4 = l in change
                    if t1 and t2 and t3 and t4 and k <= 54:
                        mtxRes[0][0] = cases(u)
                        mtxRes[0][1] = cases(o)
                        mtxRes[1][0] = cases(p)
                        mtxRes[1][1] = cases(l)
                        mas.append(k)
                        #mas.append(i)
                        #mas.append(j)
                        dic[ik] = mtxRes
                        ik = ik + 1
                        #print(mtxRes)
                        raise Exception()
                    k += 1
                mtx = mtx.transpose()
                #print(mtx)
        except:
            print(k)

        res = CompToTwo(mtxRes)
        res.name = name
        return mtxRes, mas, dic
