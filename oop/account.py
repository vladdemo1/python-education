"""This class can contain or nah current account user in restaurant"""

from user_state import UserState


class Account:
    """Main class account user - where is he have login id, password and state in BD restaurant"""

    def __init__(self, login: str, password: str, balance=0, orders=0):
        self.login = login
        self.password = password
        if balance >= 0:
            self.balance = balance
        if orders >= 0:
            self.orders = orders
        self.state = UserState.states[0]  # New

    def get_state(self):
        """This func return current status of account"""
        return self.state

    def add_balance(self, price: int):
        """In this method customer added a bonuses to balance"""
        self.balance += price

    def get_balance(self):
        """This func return current balance of account"""
        return self.balance

    def get_orders(self):
        """This func return current count orders"""
        return self.orders
