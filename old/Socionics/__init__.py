from old.Socionics.Socionics import Socionics
from old.Socionics.Psychotypes import Psychotype
from old.Socionics.Relations import Relation
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
    return res


def generate_table_16x16():
    res = '[\n'
    for name in Psychotype.get_names():
        typ = Psychotype.get(name)
        res += '['
        for other in Psychotype.get_names():
            other_typ = Psychotype.get(other)
            rel = what_is_this(Relation, typ.mult(other_typ))
            res += f'Relation.get_by_name("{rel.name}"), '
        res += '],\n'
    res += ']'
    return res
