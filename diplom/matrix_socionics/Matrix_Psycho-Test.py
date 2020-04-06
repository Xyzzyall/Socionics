import diplom.matrix_socionics.SMatrix as PsyMtx
from itertools import permutations
import numpy as np

psy = PsyMtx.Ptype.get_names()
rel = PsyMtx.Rtype.get_names()

print(PsyMtx.Ptype.get('Gu').mult(PsyMtx.Ptype.get('Gm')).__data__)
print(PsyMtx.Rtype.get('RO').__data__)


z = np.zeros((2, 2), dtype=np.complex)
compare = np.array((2, 2), bool)
l = 0
for j in range(16):
    k = 0
    l = l + 1
    print('Type', l, psy[l-1])
    for i in permutations([0, 1, 2, 3]):
        k += 1
        i = list(i)
        mtx = PsyMtx.Ptype.comp_to_two(j, i)
        compare = mtx == z
        if not compare.all():
            print(k, i)
            print(mtx)
