import diplom.matrix_socionics.SMatrix.SocMatrix as SM


class Ptype(SM.SMatrix):
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
    def get(name):
        psychotype = {
            'DK': Ptype([
                [-1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, -1, 0],
                [0, 0, 0, 1]
            ]),
            'Du': Ptype([
                [0, 0, 1, 0],
                [0, 0, 0, -1],
                [1, 0, 0, 0],
                [0, -1, 0, 0]
            ]),
            'Gu': Ptype([
                [0, 0, 0, -1],
                [0, 0, 1, 0],
                [0, -1, 0, 0],
                [1, 0, 0, 0]
            ]),
            'Rb': Ptype([
                [0, 1, 0, 0],
                [-1, 0, 0, 0],
                [0, 0, 0, 1],
                [0, 0, -1, 0]
            ]),

            'Mk': Ptype([
                [0, 1, 0, 0],
                [0, 0, -1, 0],
                [0, 0, 0, 1],
                [-1, 0, 0, 0]
            ]),
            'Gm': Ptype([
                [0, 0, 0, -1],
                [1, 0, 0, 0],
                [0, -1, 0, 0],
                [0, 0, 1, 0]
            ]),
            'Es': Ptype([
                [1, 0, 0, 0],
                [0, 0, 0, -1],
                [0, 0, 1, 0],
                [0, -1, 0, 0]
            ]),
            'Zhk': Ptype([
                [0, 0, -1, 0],
                [0, 1, 0, 0],
                [-1, 0, 0, 0],
                [0, 0, 0, 1]
            ]),

            'Np': Ptype([
                [0, 0, -1, 0],
                [0, 0, 0, 1],
                [-1, 0, 0, 0],
                [0, 1, 0, 0]
            ]),
            'Ba': Ptype([
                [1, 0, 0, 0],
                [0, -1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, -1]
            ]),
            'Dzh': Ptype([
                [0, -1, 0, 0],
                [1, 0, 0, 0],
                [0, 0, 0, -1],
                [0, 0, 1, 0]
            ]),
            'Dr': Ptype([
                [0, 0, 0, 1],
                [0, 0, -1, 0],
                [0, 1, 0, 0],
                [-1, 0, 0, 0]
            ]),

            'Ds': Ptype([
                [0, 0, 0, 1],
                [-1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, -1, 0]
            ]),
            'Sht': Ptype([
                [0, -1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, -1],
                [1, 0, 0, 0]
            ]),
            'Gb': Ptype([
                [0, 0, 1, 0],
                [0, -1, 0, 0],
                [1, 0, 0, 0],
                [0, 0, 0, -1]
            ]),
            'Gs': Ptype([
                [-1, 0, 0, 0],
                [0, 0, 0, 1],
                [0, 0, -1, 0],
                [0, 1, 0, 0]
            ])
        }
        res = psychotype[name]
        res.name = name
        return psychotype[name]
