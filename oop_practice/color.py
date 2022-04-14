"""This class contain main class about Color"""

from color_info import ColorInfo


class Color(ColorInfo):
    """This class contain main properties of color\n
       arg[0] -> id main color (0-5)\n
       arg[1] -> id other color (0-5)\n
       arg[2] -> id type color (0-5)\n"""

    def __init__(self, id_main_color: int, id_other_color: int, id_type_color: int):
        self.main_color = self.check_color_id(id_main_color)
        self.other_color = self.check_color_id(id_other_color)
        self.type_color = self.check_type_id(id_type_color)

    @staticmethod
    def check_color_id(id_color):
        """Check current color id and return correct color"""
        if 0 <= id_color <= len(ColorInfo.colors):
            return ColorInfo.colors[id_color]
        return ColorInfo.colors[0]

    @staticmethod
    def check_type_id(id_type_color):
        """Check current type id and return correct type"""
        if 0 <= id_type_color <= len(ColorInfo.types):
            return ColorInfo.types[id_type_color]
        return ColorInfo.types[4]  # Metal

    @property
    def get_main_color(self):
        """Get current main color"""
        return self.main_color

    @property
    def get_other_color(self):
        """Get current other color"""
        return self.other_color

    @property
    def get_type_color(self):
        """Get current type color"""
        return self.type_color

    def get_color_info(self):
        """Get main info about selected color"""
        text = f"Main color: {self.main_color}\n" \
               f"Other color: {self.other_color}\n" \
               f"Type color: {self.type_color}"
        return text
