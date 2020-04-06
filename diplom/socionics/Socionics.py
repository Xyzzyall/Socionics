class Psychotype:
    psycho = int
    name = str

    def __init__(self, psycho: int, name: str = None):
        self.psycho = psycho
        if name:
            self.name = name
        else:
            self.find_name()

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
    def get_by_name(name: str):
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

    def find_name(self):
        self.name = Psychotype.get_names()[self.psycho-1]

    def __getitem__(self, item: str):
        return self.get_by_name(item)

    def __str__(self):
        return self.name


class Relation:
    relation = int
    name = str

    def __init__(self, relation: int, name: str):
        self.relation = relation
        self.name = name

    @staticmethod
    def get_name(gr, i):
        relgroups = [
            ['TO', 'DU', 'AK', 'ZE'],
            ['R-', 'Z-', 'MI', 'DE'],
            ['SE', 'PO', 'KT', 'KF'],
            ['R+', 'Z+', 'PD', 'RO']
        ]
        return relgroups[gr][i]

    @staticmethod
    def get_names():
        return ['TO', 'DU', 'AK', 'ZE', 'R-', 'Z-', 'MI', 'DE', 'SE', 'PO', 'KT', 'KF', 'R+', 'Z+', 'PD', 'RO']

    @staticmethod
    def get_by_name(name):
        relation = {
            'TO': 1,
            'DU': 2,
            'AK': 3,
            'ZE': 4,

            'R-': 5,
            'Z-': 6,
            'MI': 7,
            'DE': 8,

            'SE': 9,
            'PO': 10,
            'KT': 11,
            'KF': 12,

            'R+': 13,
            'Z+': 14,
            'PD': 15,
            'RO': 16
        }
        return Relation(relation[name], name)

    def __str__(self):
        return self.name
