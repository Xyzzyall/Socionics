import Good_4x4_Comp as Comp
import Socionics.Psychotypes as Soc
import numpy as np


pType = Soc.Psychotype.get_names()
file = open('New_Psychotypes.txt', 'w')

for i in range(16):
    mtxA = Comp.CompToFour.get(pType[i]).__data__

    print(mtxA)
    s = str(mtxA)
    file.write(pType[i] + '\n')
    for index in s:
        file.write(index)
    file.write('\n')
file.close()

