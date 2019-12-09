import Socionics as Soc
import numpy as np
import Sociometrica as SM


s = SM.Sociometrica([str(i+1) for i in range(16)], Soc.Psychotype.get_names())
grades = SM.Grades({
    'TO': 0, 'DU': 1, 'AK': 1, 'ZE': 1,
    'R-': -1, 'Z-': 0, 'MI': 0, 'DE': 0,
    'SE': 1, 'PO': 1, 'KT': -1, 'KF': 0,
    'R+': 1, 'Z+': 1, 'PD': 0, 'RO': -1
})

br = SM.BinaryRelations.from_sociotypes(s, grades)
print(br)
print(grades)

balanced = SM.SocionicsGrades.balance(br.__data__, True)

print(balanced)
n = len(br.__data__)
dat = br.__data__
print(dat)
dat_balanced = dat[balanced].transpose()[balanced].transpose()

dat_numerated = np.zeros((n+1, n+1))
for i in range(n+1):
    for j in range(n+1):
        if i == 0 and j == 0:
            dat_numerated[i, j] = 0
        elif i == 0:
            dat_numerated[i, j] = balanced[j-1]+1
        elif j == 0:
            dat_numerated[i, j] = balanced[i-1]+1
        else:
            dat_numerated[i, j] = dat_balanced[i-1, j-1]

print(dat_numerated)