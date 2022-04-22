"""This mod contains main class controller"""

from model import TicTacToe
from view import View
from logs import Logs


class Controller:
    """This class manages the model and view"""

    def __init__(self, model: TicTacToe, view: View):
        self.model = model
        self.view = view

    def write_winner_to_log(self):
        """Write new log after game"""
        Logs.write_log_to_file(self.model.players,
                               self.model.time, self.model.winner, self.model.wins)

    def game(self):
        """Game active with two players"""
        # reset model and view in again=False
        self.model.reset()
        self.view.reset()

        self.view.set_players_names()  # get players names
        # set names for players
        self.model.players = [self.view.first_player, self.view.second_player]
        # set active before game
        self.model.active = True
        # until someone wins or draw
        while self.model.active:
            self.view.show_board(self.model.field)  # print current field
            self.view.next_player_move()  # get next move from user
            self.model.field = self.model.click(self.model.field, self.view.next_index_move)
        # after game show final state field
        self.view.show_board(self.model.field)
        if self.model.winner is not None:
            # write name winner if someone wins
            self.write_winner_to_log()
