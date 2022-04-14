"""This class contain main logic about tractor"""

from transport import Transport
from color import Color


class Tractor(Transport, Color):
    """This class represent of tractor and inherited from Transport\n
       arg[0] -> type of harvest (0-5)"""

    harvest_types = ("Corn", "Sunflower", "Wheat", "Beet", "Buckwheat")

    def __init__(self, type_: int, *args):
        super().__init__(*args)
        self.harvest = self.check_harvest_type_id(type_)

    @staticmethod
    def check_harvest_type_id(type_id):
        """This method for init - check about correct harvest type id"""
        if 0 <= type_id <= len(Tractor.harvest_types):
            return Tractor.harvest_types[type_id]
        return Tractor.harvest_types[0]

    def get_transport_info(self):
        text = f"This tractor is {self.owner} and from a {self.dealer} dealer.\n" \
               f"Bought for - {self.price}$ and is a harvest type - '{self.harvest}'.\n"
        return text + self.get_color_info()

    def __rshift__(self, other: str):
        """This method can give tractor to other person like [tractor >> new_owner]"""
        self.owner = Transport.get_correct_owner_name(other)
        print(f"\nThis tractor get new owner - '{self.owner}'\n")
        return self

    @classmethod
    def get_transport_name(cls):
        return cls.__name__
