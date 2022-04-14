"""This class contain main logic about trailer"""

from transport import Transport
from color import Color


class Trailer(Transport, Color):
    """This class represent of tractor and inherited from Transport\n
       arg[0] -> space of trailer in kg (int)"""

    def __init__(self, space: int, *args):
        super().__init__(*args)
        self.space = self.get_correct_space(space)
        self.free_space = 0

    @staticmethod
    def get_correct_space(space):
        """This method for init - check about correct space in kg"""
        if space > 0:
            return space
        return 1000

    def get_transport_info(self):
        text = f"This trailer for tractor " \
               f"is {self.owner} and from a {self.dealer} dealer.\n" \
               f"Bought for - {self.price}$ and space in - [{self.free_space}/{self.space}] kg.\n"
        return text + self.get_color_info()

    def __lshift__(self, other: int):
        """This method can load a trailer [trailer << some_cargo]"""
        if other <= (self.space - self.free_space):
            self.free_space += other
            print(f"\nYour cargo has been successfully added to the trailer\n"
                  f"Now in trailer [{self.free_space}/{self.space}] kg.\n")
        else:
            print("You can't add that much cargo to a trailer!")
        return self

    @classmethod
    def get_transport_name(cls):
        return cls.__name__
