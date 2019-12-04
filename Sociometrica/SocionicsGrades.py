from Socionics import Socionics
import numpy as np


class Grades:
    __h__ = np.empty(1)
    __refs__ = []

    def __init__(self, characteristics: dict, refs: set):
        self.__h__ = np.empty(len(refs))
        i = 0
        for name in refs:
            self.__h__[i] = characteristics[name]
            self.__refs__[i] = name
            i += 1

    def classify(self, relation: Socionics):
        pass


