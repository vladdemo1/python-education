"""This class contain main logic about car"""

from transport import Transport
from color import Color


class Car(Transport, Color):
    """This class represent of car and inherited from Transport\n
       arg[0] -> count places (int)"""

    def __init__(self, places: int, *args):
        self.places = self.check_correct_count_places(places)
        super().__init__(*args)

    @staticmethod
    def check_correct_count_places(count):
        """This method check correct count places for car"""
        if 2 <= count <= 50:
            return count
        return 2

    def get_transport_info(self):
        text = f"This car is {self.owner} and from a '{self.dealer}' dealer.\n" \
               f"Bought for - {self.price}$ and have a {self.places} places.\n"
        return text + self.get_color_info()

    def __iadd__(self, other: int):
        """This method add over price to current price"""
        self.price += other
        print("\nPrice changed\n")
        return self

    @classmethod
    def get_transport_name(cls):
        return cls.__name__


# print(Car.__mro__)
