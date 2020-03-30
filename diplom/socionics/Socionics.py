class Psychotype:
    psycho = 0
    name = ''

    def __init__(self, psycho, name):
        self.psycho = psycho
        self.name = name

    @staticmethod
    def get_name(gr, i):
        psychogroups = [
            ['DK', 'Du', 'Gu', 'Rb'],
            ['Mk', 'Gm', 'Es', 'Zhk'],
            ['Np', 'Ba', 'Dzh', 'Dr'],
            ['Ds', 'Sht', 'Gb', 'Gs']
        ]
        return psychogroups[gr][i]

    @staticmethod
    def get_names():
        return ['DK', 'Du', 'Gu', 'Rb', 'Mk', 'Gm', 'Es', 'Zhk', 'Np', 'Ba', 'Dzh', 'Dr', 'Ds', 'Sht', 'Gb', 'Gs']

    @staticmethod
    def get_by_name(name):
        names = {
            'DK': 1,
            'Du': 2,
            'Gu': 3,
            'Rb': 4,

            'Mk': 5,
            'Gm': 6,
            'Es': 7,
            'Zhk': 8,

            'Np': 9,
            'Ba': 10,
            'Dzh': 11,
            'Dr': 12,

            'Ds': 13,
            'Sht': 14,
            'Gb': 15,
            'Gs': 16
        }
        return Psychotype(names[name], name)


class Relation:
    pass
