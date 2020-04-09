import diplom.matrix_socionics.SMatrix as PsyMtx
from itertools import permutations
import numpy as np

psy = PsyMtx.Ptype.get_names()
rel = PsyMtx.Rtype.get_names()


def all_perms_for_all_types():
    z = np.zeros((2, 2), dtype=np.complex)
    l = 0

    for j in range(16):
        l = l + 1
        print('Type', l, psy[l - 1])
        k = 0

        for i in permutations([0, 1, 2, 3]):
            k += 1
            i = list(i)
            mtx = PsyMtx.Ptype.comp_to_two(j, i)
            compare = mtx == z
            if not compare.all():
                #print(k, i)
                print(mtx)


def for_complex_conversion_units(tup):
    z = np.zeros((4, 4), dtype=np.int)
    k = 0
    l = 0
    print('Type:', tup, psy[tup])

    for i in permutations([0, 1, 2, 3]):
        for j in permutations([0, 1, 2, 3]):
            l += 1
            m = PsyMtx.Ptype.for_complex_type_search_units_and_zeros(tup, i, j)
            compare = m == z
            if not compare.all():
                k += 1
                print('                                ', k)
                print(l, i, j)
                print(m)


def search_perm_for_complex(amount_of_equal_psy):
    z = np.zeros((4, 4), dtype=np.int)
    l = 0
    l1 = 0
    for i in permutations([0, 1, 2, 3]):
        for j in permutations([0, 1, 2, 3]):
            k = 0
            for tup in range(16):
                m = PsyMtx.Ptype.for_complex_type_search_units_and_zeros(tup, i, j)
                compare = m == z
                if not compare.all():
                    k += 1
            if k == amount_of_equal_psy:
                l1 += 1
                print('Рабочая перестановка:', i, j)
            else:
                l += 1
                print(l, 'ФЭЙЛ', i, j)
    print('Удачи:', l1)
    print('Фейл:', l)


# for i in range(16):
#     for_complex_conversion_units(i)
#     print('-------------------------------------------')
#     print('                NEXT TYPE:')
#     print('-------------------------------------------')

search_perm_for_complex(8)
