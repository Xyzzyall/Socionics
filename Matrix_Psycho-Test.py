import Good_4x4_Comp.Ptypes as Ptype
import Good_4x4_Comp.Rtypes as Rtype


psy = Ptype.Ptype.get_names()
rel = Rtype.Rtype.get_names()

for i in range(16):
    a = Ptype.Ptype.get(psy[0]).mult(Ptype.Ptype.get(psy[i]))
    print(a.name, rel[i])
    print(a.__data__)

print(Ptype.Ptype.get('Gu').mult(Ptype.Ptype.get('Gm')).__data__)
print(Rtype.Rtype.get('RO').__data__)
