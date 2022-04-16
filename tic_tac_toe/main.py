"""Contain main logic about started and play game"""

from model import TicTacToe
from view import Console
from controller import Controller


class Main:
    """Main class for start this game"""

    def __init__(self):
        self.control = Controller(TicTacToe(), Console())
        self.funcs = {0: self.control.game,
                      1: self.control.view.show_logs,
                      2: self.control.view.clear_logs,
                      3: self.control.view.exit,
                      }

    def main(self):
        """Main func for con-trolling this game"""
        while True:
            choose = self.control.view.menu()
            if choose is not False:
                self.funcs[choose]()

    def __repr__(self):
        """Get info about run view"""
        return f"This module work for '{Console.__name__}' class"


if __name__ == "__main__":
    man = Main()
    man.main()
