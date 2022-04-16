"""This mod contains abstract class view and Console version"""

import sys
from abc import ABC, abstractmethod
from logs import Logs


class View(ABC):
    """Main abstract class view"""

    @property
    @abstractmethod
    def first_player(self):
        """Like a property for get name first player"""
        raise NotImplementedError

    @property
    @abstractmethod
    def second_player(self):
        """Like a property for get name second player"""
        raise NotImplementedError

    @property
    @abstractmethod
    def next_index_move(self):
        """Get next index move for field game"""
        raise NotImplementedError

    @abstractmethod
    def show_board(self, field):
        """Show board for users"""
        raise NotImplementedError

    @abstractmethod
    def set_players_names(self):
        """Before game set names players"""
        raise NotImplementedError

    @abstractmethod
    def reset(self):
        """Before new game reset all settings"""
        raise NotImplementedError

    @abstractmethod
    def next_player_move(self):
        """Propose for user set next index move"""
        raise NotImplementedError

    @staticmethod
    def show_logs():
        """Print current logs"""
        raise NotImplementedError

    @staticmethod
    def clear_logs():
        """If user want to this - then clear logs"""
        raise NotImplementedError

    @staticmethod
    def exit():
        """Exit"""
        raise NotImplementedError

    @abstractmethod
    def menu(self):
        """Show menu for users"""
        raise NotImplementedError


class Console(View):
    """This class contain all view for play in console"""

    def __init__(self, size_board=3):
        self._states = ("Play Game", "Show Logs", "Clear Logs", "Exit")
        self._size_board = size_board
        self._first_player = None
        self._second_player = None
        self._next_index_move = None

    @property
    def first_player(self):
        """Get name first player"""
        return self._first_player

    @property
    def second_player(self):
        """Get name second player"""
        return self._second_player

    @property
    def next_index_move(self):
        """Get next index"""
        return self._next_index_move

    def reset(self):
        """Reset all settings console"""
        self.__init__()

    def show_board(self, field):
        """Print current game field"""
        print(" --- Game Field ---")
        i = 0
        for _ in range(self._size_board):
            for _ in range(self._size_board):
                print(f'{field[i]} ', end=' ')
                i += 1
            print()
        print(" ------------------")

    @staticmethod
    def check_name(name):
        """Without digits"""
        if name == '':
            return "Player"
        return name.capitalize()

    def get_name_player(self):
        """Get players names"""
        name = input("Input ur name --> ")
        return self.check_name(name)

    def set_players_names(self):
        """Set players names"""
        self._first_player = self.get_name_player()
        self._second_player = self.get_name_player()

    def next_player_move(self):
        """Set next point index on the board"""
        next_index = input("Input ur next position move (index) --> ")
        self._next_index_move = int(next_index)

    def menu(self):
        """Get something move from menu"""
        print(" --- Menu ---")
        for state in self._states:
            print(f"{state} - '{self._states.index(state)}'")
        select = input("Choose from menu [0-3] -> ")
        if select.isdigit() and (0 <= int(select) <= 3):
            return int(select)
        return False

    @staticmethod
    def show_logs():
        """Show logs from file to terminal"""
        logs = Logs()
        logs_count = logs.line_count()
        if logs_count == 0:
            print("No logs")
        else:
            print(" --- Logs ---")
            for i in range(logs_count):
                print(f"{logs.logs[i]}", end='')

    @staticmethod
    def clear_logs():
        """Clear logs"""
        print(" --- Logs cleared ---")
        Logs.clear_logs()

    @staticmethod
    def exit():
        """Exit the program"""
        sys.exit(0)
