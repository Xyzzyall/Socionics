from old import MySocioParser


class MySocioData:
    ind = 0
    types = []
    wrongs = []

    def __init__(self, line: str):
        self.ind, str_types, self.wrongs = MySocioParser.line_to_data(line)
        self.types = [MySocioData.Sociotype(typ) for typ in str_types]

    def get_max_sociotype(self):
        return max(self.types)

    class Sociotype:
        name = ''
        percentage = 0.0

        def __init__(self, data: tuple):
            self.name = data[0]
            self.percentage = float(data[1][:-1])/100

        def __str__(self):
            return ','.join([self.name, str(int(self.percentage*100)) + '%'])

        def __ge__(self, other):
            return self.percentage >= other.percentage

        def __gt__(self, other):
            return self.percentage > other.percentage

    def __str__(self):
        return '|'.join([
            str(self.ind),
            '\t'.join([str(typ) for typ in self.types]),
            '\t'.join([wrong for wrong in self.wrongs])
        ])


