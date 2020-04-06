from old.Socionics import Psychotype
from old.BinRelAnalysis import Groups


class Collective:
    size = 0

    def __init__(self, people):
        self.size = people

    def __iter__(self):
        names = Psychotype.get_names()
        #todo костыль
        gr = Groups(self.size, len(names))
        for group in gr:
            res = []
            for i in range(len(names)):
                for j in range(group[i]):
                    res.append(names[i])
            yield res
