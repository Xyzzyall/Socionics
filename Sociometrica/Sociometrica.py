import Socionics as Soc


class Sociometrica:
    __data__ = []
    __names__ = []
    __psychotypes__ = []
    __size__ = 0

    def __init__(self, names, psychotypes):
        if len(names) != len(psychotypes):
            raise IncorrectData('Size of names and psychotypes are not equal. Check input data.')

        self.__names__ = names
        self.__psychotypes__ = [Soc.Psychotype.get(name) for name in psychotypes]
        self.__size__ = len(names)

        self.__update_matrix__()

    def __update_matrix__(self):
        """Обновить матрицу интертипных отношений"""
        self.__data__ = [[Soc.what_is_this(Soc.Relation, self.__psychotypes__[i].mult(self.__psychotypes__[j])) for j in range(len(self))] for i in range(len(self))]

    def get_raw_data(self):
        return self.__data__

    def add(self, others_name, others_type):
        self.__names__.append(others_name)
        self.__psychotypes__.append(others_type)
        self.__size__ += 1
        self.__update_matrix__()

    def remove(self, name):
        i = self.__names__.index(name)
        del self.__names__[i]
        del self.__psychotypes__[i]
        self.__size__ -= 1
        self.__update_matrix__()

    def __len__(self):
        return self.__size__

    def __str__(self):
        names = [str(i+1) + ': ' + self.__names__[i] + '(' + self.__psychotypes__[i].name + ')' for i in range(self.__size__)]
        psychos = [[str(i+1)] + [elems.name for elems in self.__data__[i]] for i in range(self.__size__)]

        res = ''
        for name in names:
            res += name + '; '
        res += '\n'

        psychos = [[str(i) for i in range(self.__size__ + 1)]] + psychos    # adding numeration
        for rows in psychos:
            for elems in rows:
                res += elems + '\t'
            res += '\n'

        return res


class IncorrectData(Exception):
    pass
