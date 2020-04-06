from itertools import *


class Perms:
    obj_before = None
    left = 0
    size = 0
    i = 0
    is_last = False

    def __init__(self, before, size, is_last=False):
        self.obj_before = before
        self.size = size
        self.left = 0
        self.i = 0
        self.is_last = is_last

    def sum_chain(self):
        res = self.i
        nxt = self.obj_before
        while nxt:
            res += nxt.i
            nxt = nxt.obj_before
        return res

    def __iter__(self):
        if self.obj_before:
            self.left = self.obj_before.left - self.obj_before.i
        else:
            self.left = self.size

        for self.i in range(self.left, -1, -1):
            if self.is_last:
                if self.sum_chain() == self.size:
                    yield self.i
            else:
                yield self.i


class Groups:
    size = 0
    variants = 0
    perms = []

    def __init__(self, how_much, variants=16):
        self.size = how_much
        self.variants = variants
        self.perms.append(Perms(None, how_much))
        for i in range(1, variants - 1):
            self.perms.append(Perms(self.perms[i - 1], how_much))
        self.perms.append(Perms(self.perms[len(self.perms) - 1], how_much, is_last=True))

    def __iter__(self):
        #todo: дикий костыль
        for i0 in self.perms[0]:
            for i1 in self.perms[1]:
                for i2 in self.perms[2]:
                    for i3 in self.perms[3]:
                        for i4 in self.perms[4]:
                            for i5 in self.perms[5]:
                                for i6 in self.perms[6]:
                                    for i7 in self.perms[7]:
                                        for i8 in self.perms[8]:
                                            for i9 in self.perms[9]:
                                                for i10 in self.perms[10]:
                                                    for i11 in self.perms[11]:
                                                        for i12 in self.perms[12]:
                                                            for i13 in self.perms[13]:
                                                                for i14 in self.perms[14]:
                                                                    for i15 in self.perms[15]:
                                                                        yield i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15

        """for pr in product([i for i in range(self.size+1)], repeat=self.variants):
            if sum(pr) == self.size:
                yield pr"""

