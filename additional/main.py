"""Check all funcs and classes"""

from lazy_iterator import Chain, Zip, Product


class Main:
    """this class contains something classes for check"""

    def __init__(self):
        self.main()

    @staticmethod
    def main():
        """check work chain, zip and product"""
        # work chain
        for i in Chain('vlad', [10, 20, 30, 40], [1, 2, 3]):
            print(i, end=' ')
        print()
        # work zip
        for step in Zip("Oleksii", "NIX", (1, 5, 10)):
            print(step)
        # work product
        for i in Product([[3, 4, 5], (9, 10)]):
            print(*i)

    def __repr__(self):
        return "Check classes chain, zip and product"


if __name__ == "__main__":
    Main()
