from itertools import *


class Groups:
    size = 0
    variants = 0

    def __init__(self, how_much, variants):
        self.size = how_much
        self.variants = variants

    def __iter__(self):
        for pr in product([i for i in range(self.size+1)], repeat=self.variants):
            if sum(pr) == self.size:
                yield pr

