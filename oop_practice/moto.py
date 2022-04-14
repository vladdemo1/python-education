"""This class contain main logic about moto"""

from transport import Transport
from color import Color


class Moto(Transport, Color):
    """This class represent of moto and inherited from Transport\n
       arg[0] -> type of moto (0-5)"""

    types = ("Sport", "Touring", "Cruiser", "Dirt bike", "Standard")

    def __init__(self, type_: int, *args):
        super().__init__(*args)
        self.type_ = self.check_moto_type_id(type_)

    @staticmethod
    def check_moto_type_id(type_id):
        """This method for init - check about correct type id"""
        if 0 <= type_id <= len(Moto.types):
            return Moto.types[type_id]
        return Moto.types[4]

    def get_transport_info(self):
        text = f"This moto is {self.owner} and from a {self.dealer} dealer.\n" \
               f"Bought for - {self.price}$ and is a type - {self.type_}.\n"
        return text + self.get_color_info()

    def __le__(self, other: int):
        """This method can more or less type of moto as <= """
        # count types 5 --- from 0 to 4
        new = Moto.types.index(self.type_) - other
        if 0 <= new <= len(Moto.types):
            self.type_ = Moto.types[new]
            print(f"\nThe motorcycle type has been successfully changed to '{self.type_}'\n")
        else:
            print("\nYou cannot change the motorcycle type to the specified one!\n")
        return self

    @classmethod
    def get_transport_name(cls):
        return cls.__name__
