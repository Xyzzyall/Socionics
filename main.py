import Socionics as Soc
import numpy as np
import Sociometrica as SM

s = SM.Sociometrica(['Vasya', 'Sanya', 'Ivan', 'Kirill'], ['Np', 'Zhk', 'DK', 'Du'])
grades = SM.Grades({
    'TO': 0, 'DU': 1, 'AK': 1, 'ZE': 0,
    'R-': -1, 'Z-': -1, 'MI': -1, 'DE': 0,
    'SE': 0, 'PO': 1, 'KT': 0, 'KF': 0,
    'R+': 1, 'Z+': 1, 'PD': 0, 'RO': 0
})

br = SM.BinaryRelations.from_sociotypes(s, grades)
print(br)
print(grades)
