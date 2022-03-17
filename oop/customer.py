"""Class contain main functions for customer"""

from waiter import Waiter


class Customer:
    """This is class have all functions for customer in restaurant"""

    def __init__(self, name="Person", status=False):
        self.name = name
        self.status = status

    @staticmethod
    def waiter_call():
        """This func can return waiter for current customer"""
        return Waiter

    def get_name(self):
        """This func can return current customer name"""
        return self.name
