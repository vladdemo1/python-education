"""This module contains chain zip and product funcs"""


class Chain:
    """This class contains lazy iterator for chain func"""

    def __init__(self, *values):
        self.list = [someone for val in values for someone in val]
        self.count = 0

    def __next__(self):
        self.count += 1
        return self.next_method(self.list, len(self.list), self.count)

    def __iter__(self):
        return self

    @staticmethod
    def next_method(mass, length, count):
        """This func for all 3 classes about work next func"""
        if count < length + 1:
            return mass[count - 1]
        raise StopIteration


class Zip:
    """This class contain lazy iterator like a zip func"""

    def __init__(self, *iters):
        self.min_len = min([len(some) for some in iters])
        self.zip_mass = self.fulling_mass(iters)
        self.count = 0

    def fulling_mass(self, iters):
        """Full mass for init"""
        return [[[iter_[i]] for iter_ in iters] for i in range(self.min_len)]

    def __next__(self):
        self.count += 1
        return Chain.next_method(self.zip_mass, self.min_len, self.count)

    def __iter__(self):
        return self


class Product:
    """Like a cartesian product"""

    def __init__(self, elements):
        first, second = elements[0], elements[1]
        self.product = [[tuple([i, j]) for j in second] for i in first]
        self.count = 0

    def __next__(self):
        self.count += 1
        return Chain.next_method(self.product, len(self.product), self.count)

    def __iter__(self):
        return self
