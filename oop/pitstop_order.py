"""This class it's a child main class order and contain order for a cars"""
from order import Order


class PitStopOrder(Order):
    """This class contain funcs about pit stop orders"""

    def __init__(self, price=0, number=0, status=0, number_car=0):
        super().__init__(price, number, status)
        self.number_car = number_car

    @staticmethod
    def info():
        """Just show info about class"""
        print("This class - child of Order, work's for people on a car")

    def get_order(self):
        """This func return order message"""
        print(f"Order № {self.number} have a price = {self.price} and status = {self.status}\n"
              f"This order for car of number - {self.number_car}")
