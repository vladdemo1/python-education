"""This mod contains recursive factorial implementation"""

import sys
sys.setrecursionlimit(2000)


class Factorial:
    """Class about realization factorial by recursion"""

    def __init__(self, value: int):
        self._value = value
        self._result = self._preliminary_check()

    @property
    def result(self):
        """Get result"""
        return self._result

    def _preliminary_check(self):
        """Preliminary check about input value"""
        if self._value == 0:
            return 1
        if self._value > 0:
            return self._recursive_factorial(self._value)
        return None

    def _recursive_factorial(self, value):
        """Find factorial using our recursion"""
        if value == 1:
            return 1
        return value * self._recursive_factorial(value - 1)

    def __str__(self):
        return f'Result = {self.result}'


if __name__ == '__main__':
    FAC = Factorial(5)
    print(FAC)
