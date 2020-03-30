from old import MySocioParser as parser, Socionics as soc

psycho_map = {
    'искатель': 'DK',
    'посредник': 'Du',
    'энтузиаст': 'Gu',
    'аналитик': 'Rb',

    'инспектор': 'Mk',
    'наставник': 'Gm',
    'лирик': 'Es',
    'маршал': 'Zhk',

    'политик': 'Np',
    'критик': 'Ba',
    'предприниматель': 'Dzh',
    'хранитель': 'Dr',

    'гуманист': 'Ds',
    'администратор': 'Sht',
    'мастер': 'Gb',
    'советчик': 'Gs'
}


def mysocio_type_convert(name: str):
    return psycho_map[name.lower()]


def get_my_sociotype(data: parser.MySocioData):
    res = soc.Psychotype.get_zero()
    for typ in data.types:
        res.__data__ += soc.Psychotype.get(mysocio_type_convert(typ.name)).__data__*typ.percentage
    return res

