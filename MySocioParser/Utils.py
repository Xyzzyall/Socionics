import Socionics as soc
import MySocioParser as parser
import numpy as np


def mysocio_type_convert(name: str):
    map = {
        'искатель': 'DK',
        'посредник': 'Du',
        'энтузиаст': 'Gu',
        'аналитик': 'Rb',

        'наставник': 'Mk',
        'инспектор': 'Gm',
        'маршал': 'Es',
        'лирик': 'Zhk',

        'политик': 'Np',
        'критик': 'Ba',
        'предприниматель': 'Dzh',
        'хранитель': 'Dr',

        'администратор': 'Ds',
        'гуманист': 'Sht',
        'советчик': 'Gb',
        'мастер': 'Gs'
    }

    return map[name.lower()]


def get_my_sociotype(data: parser.MySocioData):
    res = soc.Psychotype.get_zero()
    for typ in data.types:
        res.__data__ += soc.Psychotype.get(mysocio_type_convert(typ.name)).__data__*typ.percentage
    return res

