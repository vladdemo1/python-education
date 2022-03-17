"""This class contain all price for dishes"""


class Item:
    """In this class contains prices for dishes in menu"""

    def __init__(self, quantity=1):
        self.quantity = quantity
        self.price = {"Coffee": 50, "Cake": 200, "Chocolate": 100}

    def get_quantity(self):
        """Get current count quantity of dishes"""
        return self.quantity

    def get_price(self, dishes):
        """Get price for current dishes in menu"""
        if dishes in self.price.keys():
            return self.quantity * self.price[dishes]
        return 0
