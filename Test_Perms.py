import Good_4x4_Comp as Comp
import Socionics.Psychotypes as Soc
import numpy as np


pType = Soc.Psychotype.get_names()
a = Comp.CompToFour.get(pType[4]).__data__
m = np.array(a)
print(m)
m = m[[0, 2, 1, 3]]
m = m.transpose()
m = m[[0, 2, 1, 3]]
m = m.transpose()
print(m)
