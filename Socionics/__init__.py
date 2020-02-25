from Socionics.Psychotypes import Psychotype
from Socionics.Relations import Relation
from Socionics.Socionics import Socionics
import numpy as np

def what_is_this(how_to_interpret, target):
    for name in how_to_interpret.get_names():
        obj = how_to_interpret.get(name)
        if obj == target:
            return obj
    new = how_to_interpret(target.__data___)
    new.name = '?'
    return new


def decompose(how_to_interpret, target):
    """
        ВАЖНО: считается, что все компоненты матрицы данных ровно распределены по базисам социотипа/отношений
    :return:
        процент "содержания" каждого социотипа/отношения в объекте
    """
    res = {}
    for name in how_to_interpret.get_names():
        res[name] = np.max(how_to_interpret.get(name).__data__ * target.__data__)
    print(res)
    return res
