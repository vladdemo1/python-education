"""Class TypesDishes with types for menu types"""


class TypesDishes:
    """This class's have a many types for menu"""

    types = ("Coffee", "Cake", "Chocolate")

    @staticmethod
    def show_types():
        """This method shows all types"""
        print(TypesDishes.types)

    @staticmethod
    def info():
        """Main info about class"""
        print("This class needed to contain types for menu")


if __name__ == "__main__":
    TypesDishes.info()
    TypesDishes.show_types()
