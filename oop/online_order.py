"""This class it's a child main class order and contain order for a web"""
from order import Order


class OnlineOrder(Order):
    """This class contain funcs about web order"""

    def __init__(self, price=0, number=0, status=0, address="Kharkov"):
        super().__init__(price, number, status)
        self.address = address

    @staticmethod
    def info():
        """Func show info"""
        print("This class - child of Order, work's for web")

    def get_order(self):
        """This func return order message"""
        print(f"Order № {self.number} have a price = {self.price} and status = {self.status}\n"
              f"This order will be send to address - {self.address} str.")
