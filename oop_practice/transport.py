"""This class contain main logic of transport"""


class Transport(object):
    """This class contain main properties of cars\n
       arg[0] -> owner (str)\n
       arg[1] -> dealer (0-6)\n
       arg[2] -> price (int)"""

    dealers = ("Tesla", "Dodge", "BMW", "Mercedes", "Audi", "Porsche")

    def __init__(self, owner: str, dealer: int, price: int, *args):
        super().__init__(*args)
        self.owner = self.get_correct_owner_name(owner)
        self.dealer = self.get_correct_dealer(dealer)
        self.price = self.get_correct_price(price)

    @staticmethod
    def get_correct_owner_name(name_owner):
        """This method return correct """
        name = ''.join([x for x in name_owner if not x.isdigit()])
        return name.capitalize()

    @staticmethod
    def get_correct_price(price):
        """Check current price and return correct value for price"""
        if price > 0:
            return price
        return 1_000_000

    @staticmethod
    def get_correct_dealer(id_dealer):
        """Check current dealer id and return correct dealer"""
        if 0 <= id_dealer <= len(Transport.dealers):
            return Transport.dealers[id_dealer]
        return Transport.dealers[0]

    @property
    def get_owner(self):
        """Get current name owner"""
        return self.owner

    @property
    def get_dealer(self):
        """Get current name dealer"""
        return self.dealer

    def __get__(self, obj,  objtype):
        """Can get a price (descriptor)"""
        print("Get a price")
        return self.price

    def get_transport_info(self):
        """Get main info about this transport"""
        return f"{self.owner} bought this transport " \
               f"from a {self.dealer} dealer!"

    @classmethod
    def get_transport_name(cls):
        """Get current class name"""
        return cls.__name__


class CheckClass(object):
    """Test class about descriptor"""
    tr = Transport("Vlad", 2, 1000000)


if __name__ == "__main__":
    get_price = CheckClass()
    print(get_price.tr)
