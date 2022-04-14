"""This class contain main logic about bike"""

from transport import Transport
from color import Color


class Bike(Transport, Color):
    """This class represent of bike and inherited from Transport\n
       arg[0] -> weight (int)"""

    def __init__(self, weight: int, *args):
        super().__init__(*args)
        self.weight = self.get_correct_weight(weight)

    @staticmethod
    def get_correct_weight(weight):
        """This method for init - check about correct weight in kg"""
        if weight > 0:
            return weight
        return 10

    def get_transport_info(self):
        text = f"This bike is {self.owner} and from a {self.dealer} dealer.\n" \
               f"Bought for - {self.price}$ and weighs - {self.weight} kg.\n"
        return text + self.get_color_info()

    def __eq__(self, other: str):
        """This method can paint a bike"""
        # Use method from class Transport for get correct name color
        color = Transport.get_correct_owner_name(other)
        if color in Color.colors:
            self.main_color = color
            print(f"The bike painted to choose color -> '{self.main_color}'\n")
        else:
            print("Selected color doesn't exists in the standard set!\n")
        return self

    @classmethod
    def get_transport_name(cls):
        return cls.__name__
