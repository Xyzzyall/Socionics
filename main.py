import Socionics as Soc
import numpy as np
import Sociometrica as SM
import BinRelAnalysis as BA


s = SM.Sociometrica([str(i+1) for i in range(16)], Soc.Psychotype.get_names())
grades = SM.Grades({
    'TO': 0, 'DU': 1, 'AK': 1, 'ZE': 1,
    'R-': 1, 'Z-': 1, 'MI': 1, 'DE': 0,
    'SE': 0, 'PO': 0, 'KT': 0, 'KF': 0,
    'R+': 0, 'Z+': 0, 'PD': 0, 'RO': -1
})

br = SM.BinaryRelations.from_sociotypes(s, grades)
print(br)
print(grades)

test = np.array([
    [0,  1,  0,  0,  1,  1,  0, -1,  1,  1],
    [1,  0,  1,  1,  1,  1, -1, -1,  0,  1],
    [0,  1,  0,  0,  1,  1, -1,  0,  1,  1],
    [0,  1,  0,  0,  1,  1, -1,  0,  1,  1],
    [1,  1,  1,  1,  0,  0,  0,  0,  0,  0],
    [1,  1,  1,  1,  0,  0, -1,  0,  0,  1],
    [-1,  0,  0,  0,  0,  0,  0,  1,  0, -1],
    [-1, -1,  0,  0,  0, -1,  1,  0, -1, -1],
    [1,  0,  1,  1,  1,  0,  0,  0,  0,  0],
    [1,  1,  1,  1,  0,  1,  0, -1,  0,  0]
]) + np.eye(10,10)

data = br.__data__
balanced = SM.balance(data, u=False)
dat_balanced = data[np.ix_(balanced, balanced)]
print(balanced)
print(dat_balanced)
print(SM.check_blocks(dat_balanced))

prd = list(BA.Groups(2, 16))
print(len(prd))
for pr in prd:
    print(pr)
#n = len(br.__data__)
#dat = br.__data__
#print(dat)
#dat = test.copy()
#n = len(dat)
#dat_balanced = dat[np.ix_(balanced, balanced)]#dat[balanced].transpose()[balanced].transpose()
