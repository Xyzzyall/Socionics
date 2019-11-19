import numpy as np
from scipy import optimize as opt
import scipy as sp
import random
import copy


class Relation:
    __data__ = np.empty((8, 8))
    name = ''

    def __init__(self, data):
        self.__data__ = np.array(data)

    def approximate(self, target):
        x = target
        x1 = x[0:8]
        x2 = np.transpose(x[8:16])
        rel = self.__data__ + np.ones((8, 8))

        return np.matmul(np.matmul(x1, rel), x2)

    @staticmethod
    def get_name(gr, i):
        relgroups = [
            ['TO', 'DU', 'AK', 'ZE'],
            ['R-', 'Z-', 'MI', 'DE'],
            ['SE', 'PO', 'KT', 'KF'],
            ['R+', 'Z+', 'PD', 'RO']
        ]
        return relgroups[gr][i]

    @staticmethod
    def get_names():
        return ['TO', 'DU', 'AK', 'ZE', 'R-', 'Z-', 'MI', 'DE', 'SE', 'PO', 'KT', 'KF','R+', 'Z+', 'PD', 'RO']

    @staticmethod
    def get(name):
        relation = {
            'TO': Relation([
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1]
            ]),
            'DU': Relation([
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0]
            ]),
            'AK': Relation([
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0]
            ]),
            'ZE': Relation([
                [0, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0]
            ]),

            'R-': Relation([
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0]
            ]),
            'Z-': Relation([
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0]
            ]),
            'MI': Relation([
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0]
            ]),
            'DE': Relation([
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0]
            ]),

            'SE': Relation([
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0]
            ]),
            'PO': Relation([
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0]
            ]),
            'KT': Relation([
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0]
            ]),
            'KF': Relation([
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0]
            ]),

            'R+': Relation([
                [0, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 0, 0]
            ]),
            'Z+': Relation([
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0]
            ]),
            'PD': Relation([
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0]
            ]),
            'RO': Relation([
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1]
            ])
        }
        return relation[name]

    @staticmethod
    def find_magic_numbers(target):
        names = Relation.get_names()

        jac_relmats = [[[] for i in range(16)] for i in range(16)]
        for i1 in range(16):
            rel = Relation.get(names[i1]).__data__ + np.ones((8, 8))
            for step in [True, False]:
                for i2 in range(8):
                    m = np.zeros((8, 8))
                    if step:
                        m[i2, :] = rel[i2, :]
                    else:
                        m[:, i2] = rel[:, i2]
                    jac_relmats[i1][i2 + (8 if not step else 0)] = m

        def jacobian(x):
            a = np.zeros((16, 16))
            for i1 in range(16):
                for i2 in range(16):
                    x_buf = np.array(x)
                    x_buf[i2] = 1.0
                    a[i1, i2] = np.matmul(np.matmul(x_buf[0:8], jac_relmats[i1][i2]), np.transpose(x_buf[8:16]))
            return a

        def func1(x):
            a = np.zeros(16)
            x1 = x[0:8]
            x2 = np.transpose(x[8:16])
            for i in range(16):
                rel = Relation.get(names[i]).__data__ + np.ones((8, 8))
                a[i] = np.matmul(np.matmul(x1, rel), x2) - target[i]
            return a

        mat = np.zeros((8, 8))
        for i1 in range(8):
            for i2 in range(8):
                mat[i1, i2] = (target[i1] + target[i2])/2
        print(mat)

        def func(x):
            a = np.zeros(16)
            x1 = x[0:8]
            x2 = np.transpose(x[8:16])
            for i in range(16):
                rel = Relation.get(names[i]).__data__
                a[i] = np.matmul(np.matmul(x1, np.matmul(rel, mat)), x2) - target[i]

            return a

        x0 = np.array(target)
        #x0 = np.ones(16)
        #x0 = np.array([random.randrange(-10,10)/10 for i in range(16)])
        sol = opt.root(func, x0, jac=jacobian, method='hybr')
        #sol = opt.toms748(func, -1*x0, x0)
        #print(sol)

        x1 = sol.x[0:8]
        x2 = np.transpose(sol.x[8:16])
        print(np.matmul(np.matmul(x1, np.matmul(Relation.get('TO').__data__, mat)), x2))

        return sol.x


target = np.array([1, -1, -1, 0, 1, 0, 1, -1, -1, 1, 0, 1, 0, 1, -1, 1])
target = np.array([0, 1, -1, 1,
                   0, 1, 1, 1,
                   1, 1, 1, 0,
                   1, -1, 1, 0])
#target = range(16)

x = Relation.find_magic_numbers(target)

out_x = np.array([x[0:4], x[4:8], x[8:12], x[12:16]])

print(out_x)

names = Relation.get_names()
res = np.zeros(16)
for i in range(16):
    res[i] = Relation.get(names[i]).approximate(x)

ddd = np.zeros(16)
for i in range(16):
    ddd[i] = res[i]-target[i]
    print(str(int(np.round(res[i])) == target[i]) + '   ' + str(ddd[i]) + '       ' + str(res[i]))

print()
print(np.std(ddd))
