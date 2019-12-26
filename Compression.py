import Socionics as Soc
import Conversion as Conv


mtxA = Conv.ConversionPsychotype.get('Gs').__data__

mtxB = Soc.Psychotype.get('Du').__data__
relDu = Soc.Relation.get('DU').__data__

print(mtxA)
#print(mtxB)
#print(relDu)