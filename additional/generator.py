"""This mode contains generator fibonacci numbers"""


class Fibonacci:
    """Class like a generator fibonacci numbers"""

    def __init__(self):
        self.first = 1
        self.second = 1
        self.fibo = self.fibochka

    def fibochka(self):
        """Get next number from fibonacci"""
        first, second = self.first, self.second
        while True:
            yield first
            first, second = second, first + second

    def __repr__(self):
        return f"<name_class={self.__class__.__name__}>"


BOCHKA = Fibonacci()
MOD = BOCHKA.fibo()

print(next(MOD))  # 1
print(next(MOD))  # 1
print(next(MOD))  # 2
print(next(MOD))  # 3
