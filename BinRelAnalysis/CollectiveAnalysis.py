import Sociometrica as SM
import numpy as np


class CollectiveAnalysis:
    collective = None
    grades = None

    def __init__(self, collective, grades):
        self.collective = collective
        self.grades = grades

    def __iter__(self):
        for c in self.collective:
            bin_rel = SM.BinaryRelations.from_sociotypes(SM.Sociometrica(c, c), self.grades)
            dat = bin_rel.__data__
            inds = SM.balance(dat)
            dat = dat[np.ix_(inds, inds)]
            yield None, SM.check_blocks(dat)

