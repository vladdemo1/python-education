"""This class contain main waiter in restaurant"""

from order import Order
from online_order import OnlineOrder
from pitstop_order import PitStopOrder


class Waiter:
    """Class Waiter contains main func for work waiters"""

    def __init__(self, location="Hall", status=True):
        self.location = location
        self.status = status

    @staticmethod
    def check(price: int, way):
        """Give check for customer
        About way:
        1 - in restaurant
        2 - online
        3 - pitstop"""
        order = Order(price)
        if way[0] == "online":
            order = OnlineOrder(price=price, address=way[1])
        if way[0] == "pitstop":
            order = PitStopOrder(price=price, number_car=way[1])
        return order

    def get_location(self):
        """Get current location waiter"""
        return self.location
