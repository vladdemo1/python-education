"""Class Restaurant - Main class"""

import time

from customer import Customer
from account import Account
from waiter import Waiter
from menu import Menu
from line_item import Item
from user_profile import UserProfile


class Restaurant:
    """Main class in program - Restaurant"""

    waiter = Waiter()
    user_profile = UserProfile()

    def __init__(self, name="Buffet", address="University"):
        self.name = name
        self.address = address

    @staticmethod
    def get_account(accounts):
        """Gets all accounts"""
        print("Accounts:")
        for i in accounts:
            print(i)

    @staticmethod
    def info():
        """Show all info about main class"""
        print("It's a main class - Restaurant")


def choose_restaurant(rest):
    """Function can give a chance choose name and address restaurant"""
    re_rest = input("Do u want re select new restaurant?\n"
                    "Yes - something letter\n"
                    "No - just Enter\n"
                    "---> ")
    if re_rest != "":
        rest.name = input("Please, choose a restaurant (name) -> ")
        rest.address = input("Choose a address restaurant -> ")

    return rest


def first_restaurant():
    """Stock info about new customer"""
    new_restaurant = Restaurant()

    print("Hello! Now u can relax in our restaurant net")
    # choose rest
    new_restaurant = choose_restaurant(new_restaurant)

    print(f"Now you can buy something in main restaurant - {new_restaurant.name}")
    input("Please! Press Enter!")

    name = input("Okay! What is ur name?  -> ")
    print(f"{name}, now we in rest '{new_restaurant.name}' on {new_restaurant.address} str.")
    print("After this level we can call waiter and select different dishes")
    input("Press Enter!\n")
    # rename customer in userprofile
    new_restaurant.user_profile.name = name
    return new_restaurant, name


def create_account(default_name):
    """If customer don't have an account, in this func he's can make it"""
    select = input("Do u want a create account? "
                   "If Yes - input something or Not - just press Enter --> ")
    if select == "":
        new_account = Account(default_name, "123")
        return new_account
    print("For ur account u must select something login and password")

    login = input("Input ur login -> ")
    if login.isdigit():
        login = default_name
    password = input("input ur password -> ")
    new_account = Account(login, password)

    print("Well done! Account was created!")
    input("Press Enter to continue...")
    return new_account


def online_order(username):
    """Customer's can make an order from account"""
    print(f"Hello, {username}!")
    address = input("Before current order, please, input ur address -> ")
    return address


def pitstop_order(username):
    """If customer drive a car to this restaurant, he's need tell ur number car"""
    number_car = input(f"Hi, {username}! U have a nice car! What is number car?  -> ")
    return number_car


def get_dishes(username):
    """Get all dishes from types dishes and return it"""
    menu = Menu()
    print("\nMenu:")
    dishes = menu.get_all_dishes()
    items = ""
    for i in range(menu.get_count_dishes()):
        items += f"{i} - {dishes[i]}\n"
    print(items)

    way = select_way()

    get_way = get_data_way(way, username)
    if get_way:
        return dishes, get_way
    return dishes, way


def select_way():
    """Select method of buy some dishes
    1 - in restaurant
    2 - online
    3 - pitstop"""

    print("Please, select way:\n"
          "1 - in restaurant\n"
          "2 - online\n"
          "3 - pitstop\n")
    way = int(input("--> "))
    if way == 2:
        way = "online"
    elif way == 3:
        way = "pitstop"
    else:
        way = "restaurant"
    return way


def get_data_way(way, username):
    """Get current data for select way"""
    if way == "restaurant":
        return way
    if way == "online":
        address = online_order(username)
        return way, address
    if way == "pitstop":
        number_car = pitstop_order(username)
        return way, number_car
    return False


def show_menu(username):
    """Main function about shows current menu for customer and her """

    dishes, way = get_dishes(username)

    selected_dishes = dict()
    while True:
        select_number = int(input("Input the select dishes -> "))
        if 0 <= select_number <= 2:
            name_dishes = dishes[select_number]
            count_dishes = int(input(f"Input count selected {name_dishes} -> "))
        else:
            print("Please! Select correct number of dishes")
            continue

        if count_dishes > 100 or count_dishes < 0:
            count_dishes = 1

        if dishes[select_number] in selected_dishes.keys():
            selected_dishes[name_dishes] += count_dishes
        else:
            selected_dishes[name_dishes] = count_dishes

        again = input("Do u want select something too?\n"
                      "Enter - No\n"
                      "Something letter - Yes\n")
        if again == "":
            break
    return selected_dishes, way


def get_price(select_in_menu):
    """This function can return current price of dishes"""
    line_items = Item()
    price = 0
    for dishes in select_in_menu.keys():
        line_items.quantity = select_in_menu[dishes]
        price += line_items.get_price(dishes)
    return price


def get_dishes_from_order(selected_dishes):
    """Process waiting for dishes from order to customer"""
    print("Please wait. Your Order in progress on kitchen!")
    print("[", end='')
    for _ in range(20):
        second = len(selected_dishes.keys())
        time.sleep(second)
        print(f"#", end='')
    print("] Order was completed!\n")
    print("Ur order:")
    for dishes, count in selected_dishes.items():
        print(f"{dishes} - {count} pieces")
    print("\nThanks for the order!")


def make_order_again():
    """After all movies, customer can make order again, if his needed in this"""
    choose = input("\nDo u want a make order again?\n"
                   "Yes - input some letter\n"
                   "No - press Enter\n"
                   "---> ")
    if choose == "":
        return False
    return True


def finish():
    """For end program"""
    print("Thanks for the visit.")
    print("Have a good day!")


def main():
    """Main func for this project"""
    # for while state
    active = True

    # create new restaurant and select name customer
    restaurant, name_customer = first_restaurant()

    # create new customer
    customer = Customer(name_customer)

    # create or not account for customer in restaurant
    account = create_account(restaurant.user_profile.name)

    while active:

        # time to show main menu for customer and select way
        select_in_menu, way = show_menu(name_customer)

        # get a current price order
        current_price = get_price(select_in_menu)

        # add bonuses to balance
        account.add_balance(current_price)

        # get a check from waiter
        check = customer.waiter_call().check(current_price, way)

        check.get_order()

        # print current order for customer
        get_dishes_from_order(select_in_menu)

        # choose again
        active = make_order_again()
    # end
    finish()


if __name__ == "__main__":
    main()
