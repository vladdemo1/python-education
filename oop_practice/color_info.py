"""This abstract class contain main class Info about Selected Color and type"""

from abc import ABC, abstractmethod


class ColorInfo(ABC):
    """This abstract class have main info about types for colors"""

    colors = ("Black", "White", "Red", "Green", "Blue")
    types = ("Gradient", "Matte", "Pearl", "Metallic", "Metal")

    @abstractmethod
    def get_color_info(self):
        """This method can be overridden in class color"""
        print("About colors, they have the following types:")
        for type_ in ColorInfo.types:
            print(f"--> {type_}")

    @staticmethod
    def info_about_select():
        """This method as a hint."""
        print("If u dont choose the type of painting, this type will default to Metal!")
