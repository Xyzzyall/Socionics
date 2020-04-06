import diplom.matrix_socionics.SMatrix as PsyMtx


psy = PsyMtx.Ptype.get_names()
rel = PsyMtx.Rtype.get_names()

for i in range(16):
    a = PsyMtx.Ptype.get(psy[0]).mult(PsyMtx.Ptype.get(psy[i]))
    print(a.name, rel[i])
    print(a.__data__)

print(PsyMtx.Ptype.get('Gu').mult(PsyMtx.Ptype.get('Gm')).__data__)
print(PsyMtx.Rtype.get('RO').__data__)
