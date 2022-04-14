"""Here is the class implementation"""

# pylint: disable=C0103
# By this error pylint cursed at lower case.
# pylint: disable=W0104
# This about custom magic methods

import sys
from transport import Transport
from car import Car
from moto import Moto
from bike import Bike
from tractor import Tractor
from trailer import Trailer
from color import Color

transport_types = ("Car", "Moto", "Bike", "Tractor", "Trailer")
all_types_review = {"Car types": transport_types,
                    "Car dealers": Transport.dealers,
                    "Colors": Color.colors,
                    "Color types": Color.types,
                    "Moto types": Moto.types,
                    "Harvest types for tractor": Tractor.harvest_types,
                    }
all_transport = []  # contain all transports


def show_all_types(mass_types, name_type):
    """Show all types"""
    print(f" --- Popular {name_type} --- ")
    for id_type in range(len(mass_types)):
        print(f"| {mass_types[id_type]} -> [{id_type}] ", end='')
    print("|")


def welcome():
    """Standard message for user"""
    print("\nHi and welcome to our transport dealership!")
    print("Today u can become a happy owner of cool "
          "vehicles from different manufacturers!")
    for key, value in all_types_review.items():
        show_all_types(value, key)


def select_transport_type():
    """Give for user as chance choose transport type"""
    owner_name = input("\nBefore buying the best transport "
                       "in the world introduce yourself, "
                       "what is your name? --> ")
    selected_transport_type = int(input(f"Thanks for the answer, {owner_name}!\n"
                                        f"Whats type transport do u want? [Id type transport] -> "))
    return owner_name, selected_transport_type


def choose_dealer():
    """In this func user can choose something dealer"""
    return int(input("Please, choose dealer id --> "))


def choose_price():
    """In this func user input price for selected transport"""
    return int(input(f"Enter purchase price --> "))


def choose_color():
    """In this method user selected paint for transport"""
    main_color_id = int(input("Main color id --> "))
    other_color_id = int(input("Other color id --> "))
    type_color_id = int(input("Type color id --> "))
    return main_color_id, other_color_id, type_color_id


def choose_car_places():
    """This func for user choose car places"""
    return int(input("Choose car count places --> "))


def choose_moto_type():
    """This func if user buy a moto"""
    return int(input("Input moto type id --> "))


def choose_bike_weight():
    """This func if user buy a bike"""
    return int(input("Input bike weight --> "))


def choose_tractor_harvest():
    """This func if user buy a tractor"""
    return int(input("Input harvest id for tractor --> "))


def choose_trailer_space():
    """This func if user buy a trailer"""
    return int(input("Input trailer space in kg --> "))


def show_correct_transport_additional(transport_type):
    """Depending on the type of transport"""
    if transport_type == "Car":
        return choose_car_places()
    if transport_type == "Moto":
        return choose_moto_type()
    if transport_type == "Bike":
        return choose_bike_weight()
    if transport_type == "Tractor":
        return choose_tractor_harvest()
    if transport_type == "Trailer":
        return choose_trailer_space()


def create_new_transport(transport_type, *args):
    """This func created new transport and return it"""
    if transport_type == "Car":
        return Car(*args)
    if transport_type == "Moto":
        return Moto(*args)
    if transport_type == "Bike":
        return Bike(*args)
    if transport_type == "Tractor":
        return Tractor(*args)
    if transport_type == "Trailer":
        return Trailer(*args)


def available_actions():
    """Return next action from user"""
    print("\n --- And now u can next actions ---")
    actions = ["Show u transport [0]", "Buy new transport [1]",
               "Change something feature for transport [2]", "Exit [3]"]
    for act in actions:
        print(act)
    select = int(input("Input selected action --> "))
    return select if 0 < select <= 3 else 0


def show_all_transport():
    """This func for action requests"""
    print()
    for tr in all_transport:
        print(tr.get_transport_info())
        print()


def choose_id_transport_action():
    """Choose current transport from mass of all transport"""
    print(f"Choose id from active transport [from 0 to {(len(all_transport) - 1)}]")
    selected_id = int(input("Input selected id --> "))
    return selected_id if 0 <= selected_id < len(all_transport) else 0


def action_requests():
    action = available_actions()
    if action == 0:
        show_all_transport()  # show all transport from mass
    if action == 1:
        main()  # new buy a car
    if action == 2:
        selected_id = choose_id_transport_action()
        make_transport_action(all_transport[selected_id])
    if action == 3:
        print("Thanks! See u soon!")
        sys.exit(0)


def make_transport_action(transport):
    """Change settings transport like a += or <= or == or >> or <<"""
    transport_name = transport.get_transport_name()
    if transport_name == "Car":
        price_up = int(input("Input price to up -> "))
        change_car_price(transport, price_up)
    if transport_name == "Moto":
        change_type = int(input("Input count level up for type -> "))
        moto_type_up(transport, change_type)
    if transport_name == "Bike":
        new_color = input("Input name new color for bike -> ")
        bike_change_color(transport, new_color)
    if transport_name == "Tractor":
        name_new_owner = input("Input name new owner for tractor -> ")
        tractor_change_owner(transport, name_new_owner)
    if transport_name == "Trailer":
        cargo_in_kg = int(input("Input a new cargo in kg for trailer -> "))
        add_cargo_to_trailer(transport, cargo_in_kg)


def change_car_price(car, price_up):
    """Main sub func for Car"""
    car += price_up
    return car


def moto_type_up(moto, level_up):
    """Change type moto like to up or down"""
    moto <= level_up
    return moto


def bike_change_color(bike, new_color):
    """Change color for a bike"""
    bike == new_color
    return bike


def tractor_change_owner(tractor, name_new_owner):
    """Change owner for tractor"""
    tractor >> name_new_owner
    return tractor


def add_cargo_to_trailer(trailer, cargo_kg):
    """Add cargo in kg to trailer"""
    trailer << cargo_kg
    return trailer


def finish():
    print("Thanks!")


def main():
    """Main func in this module"""

    owner_name, transport_type_id = select_transport_type()
    dealer_id = choose_dealer()
    price = choose_price()
    main_color_id, other_color_id, type_color_id = choose_color()
    additional_value = show_correct_transport_additional(transport_types[transport_type_id])

    new_transport = create_new_transport(transport_types[transport_type_id], additional_value,
                                         owner_name, dealer_id, price, main_color_id,
                                         other_color_id, type_color_id)
    all_transport.append(new_transport)
    while True:
        action_requests()


if __name__ == "__main__":
    welcome()
    main()
