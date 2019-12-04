from Sociometrica import Sociometrica
import numpy as np


class BinaryRelations:
    __data__ = np.empty((1, 1))
    __names__ = []

    def __init__(self, data, names):
        self.__data__ = data
        self.__names__ = names.copy()

    @staticmethod
    def from_sociotypes(sociotypes: Sociometrica, ):
        pass





