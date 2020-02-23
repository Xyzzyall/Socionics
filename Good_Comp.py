import Good_4x4_Comp as Comp
import Socionics.Psychotypes as Soc
import numpy as np


pType = Soc.Psychotype.get_names()
# file = open('New_Psychotypes.txt', 'w')
#
# for i in range(16):
#     mtxA = Comp.CompToFour.get(pType[i]).__data__
#
#     print(mtxA)
#     s = str(mtxA)
#     file.write(pType[i] + '\n')
#     for index in s:
#         file.write(index)
#     file.write('\n')
# file.close()

# a = {}
# for i in range(16):
#     _, mas, _ = Comp.CompToTwo.get(pType[i])
#     a[pType[i]] = mas
# print(a)
# for i in range(16):
#     print(set(a[pType[0]]) & set(a[pType[i]]))

dic = {}
dict2 = {}
for i in range(16):
    print(pType[i])
    mtxA, mas, dic[i] = Comp.CompToTwo.get(pType[i])
    print(dic[i])

# count = 0
# for i in range(16):
#     for j in range(25):
#         y = dic[0][j] in dic[i][j]
#         if not y :
#             count += 1
#             print(pType[i], j)
# print(count/(j+1))

print(dic[0][0] in dic[0][2])

for i in range(16):
    dict2[i] = set(dic[i])
print(dict2)
