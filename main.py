import Socionics as Soc
import numpy as np

a = Soc.Psychotype.get('Np')
a1 = Soc.Psychotype.get('Np')
b = Soc.Psychotype.get('Dr')
c = a.mult(b)

print(str(a) + ' ' + str(b))
print(str(c) + ' ' + str(Soc.what_is_this(Soc.Relation, c)))
