"""This model contains main class about game"""

import math
from datetime import datetime


class TicTacToe:
    """This class contains field and etc"""

    def __init__(self, players=None, size=9):
        if players is None:
            players = ['Player', 'Player']
        self.field = self.make_empty_field(size)
        self._time = datetime.today().replace(microsecond=0)
        self.active = False
        self._counter = 0
        self._winner = None
        self.players = players
        self._wins = [0, 0]

    def reset(self):
        """Reset all settings game"""
        self.__init__()

    @property
    def time(self):
        """Get current time"""
        return self._time

    @property
    def counter(self):
        """Get counter"""
        return self._counter

    @property
    def winner(self):
        """Get winner"""
        return self._winner

    @property
    def wins(self):
        """Get all wins"""
        return self._wins

    def make_empty_field(self, size: int):
        """Get empty field like list"""
        # if the correct field (matrix) size
        if self.is_square(size):
            return ['#' for _ in range(size)]
        return ['#' for _ in range(9)]

    @staticmethod
    def is_square(num):
        """Check real square"""
        if int(math.sqrt(num) + 0.5) ** 2 == num:
            return True
        return False

    def click(self, field, index):
        """Player clicked to game field"""
        point = "X" if self._counter % 2 == 0 else "O"
        if self.active and field[index] == '#':
            field[index] = point
            self._counter += 1
            if self.check_win(point, field):
                self._winner = self.win(point)
        return field

    @staticmethod
    def check_win(point, field):
        """Check win for unregistered size field"""
        nope = "#"
        size_slice = int(math.sqrt(len(field)))
        # check lines
        for i in range(size_slice):
            if all((point == char != nope for char in
                    field[size_slice * i:size_slice * i + size_slice])):
                return True
        # check left diagonal
        normal_diagonal = [field[i] for i in range(0, len(field), size_slice + 1)]  # tyt +1
        if all((point == char != nope for char in normal_diagonal)):
            return True
        # check right diagonal
        reverse_diagonal = []
        for i in range(size_slice):
            for item in reversed(field[size_slice * i:size_slice * i + size_slice]):
                reverse_diagonal.append(item)
        if all((point == char != nope for char in reverse_diagonal)):
            return True
        # if not search
        return False

    def win(self, point):
        """If player win, get name winner"""
        winner = self.get_name_winner(point)
        self.active = False
        return winner

    def get_name_winner(self, point):
        """get name winner by point"""
        if point == "X":
            self._wins[0] += 1
            return self.players[0]
        self._wins[1] += 1
        return self.players[1]
