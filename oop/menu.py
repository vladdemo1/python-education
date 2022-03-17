"""This class contain main types dishes"""

from types_dishes import TypesDishes


class Menu:
    """This is class have main types of dishes"""

    def __init__(self, select_type=0):
        """Numbers some dishes:
        0 - Coffee
        1 - Cake
        2 - Chocolate"""
        if 0 <= select_type <= 3:
            self.select_type = TypesDishes.types[select_type]

    def get_type(self):
        """Return current selected typy of dishes"""
        return self.select_type

    @staticmethod
    def get_all_dishes():
        """Return all types of dishes"""
        return TypesDishes.types

    @staticmethod
    def get_count_dishes():
        """Return count dishes"""
        return len(TypesDishes.types)
