from Socionics.Psychotypes import Psychotype
from Socionics.Relations import Relation
from Socionics.Socionics import Socionics


def what_is_this(how_to_interpret, target):
    for name in how_to_interpret.get_names():
        obj = how_to_interpret.get(name)
        if obj == target:
            return obj
    return None
