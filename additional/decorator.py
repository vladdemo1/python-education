"""This mod contains class decorator"""

import logging
from datetime import datetime
from functools import wraps


class Decorator:
    """This decorator logging time executed program"""

    def __init__(self):
        self.file_name = 'time.log'

    def write_log_to_file(self, time, func_name):
        """Write log when the func is executed"""
        logging.basicConfig(filename=self.file_name, filemode='a', level=logging.DEBUG)
        logging.debug(f"{time} - The function has been executed, name = '{func_name}'")

    def __call__(self, func):
        """This decorator check time go func"""
        @wraps(func)
        def wrapper():
            func()
            time = datetime.today().replace(microsecond=0)
            self.write_log_to_file(time, func.__name__)
        return wrapper


@Decorator()
def print_bob():
    """Print Bob name"""
    print("BOB")


if __name__ == "__main__":
    print_bob()  # call func and write time executed
