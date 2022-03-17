"""Class OrderStatus with statuses for orders"""


class OrderStatus:
    """This class's have a many statuses for orders"""

    statuses = ("New", "Hold", "Shipped", "Delivered", "Closed")

    @staticmethod
    def show_statuses():
        """This func show's all statuses"""
        print(OrderStatus.statuses)

    @staticmethod
    def info():
        """Main info about class"""
        print("This class needed to contain statuses for order")


if __name__ == "__main__":
    OrderStatus.info()
    OrderStatus.show_statuses()
