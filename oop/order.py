"""This class Order contain main func about functions orders in restaurant"""

from order_status import OrderStatus


class Order:
    """Main class about order in restaurant"""

    def __init__(self, price=0, number=0, status=0):
        if price >= 0:
            self.price = price
        if number >= 0:
            self.number = number
        if 0 <= status <= 4:
            self.status = OrderStatus.statuses[status]

    def get_order(self):
        """This func return order message"""
        print(f"Order № {self.number} have a price = {self.price} and status = {self.status}")

    @staticmethod
    def info():
        """This func show info about class"""
        print("This class contain main function about order")
