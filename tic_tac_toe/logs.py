"""This module for read log files"""

# pylint: disable=W1401
# without explicitly specifying an encoding
# pylint: disable=W1514

import re
import os
import logging.config

FILE_NAME = 'game.log'  # log file


class Logs:
    """Class about logs after game"""

    def __init__(self):
        self._logs = self.read_logs()
        self._count_logs = self.line_count()

    @property
    def logs(self):
        """Get logs like list"""
        return self._logs

    @property
    def count_logs(self):
        """Get count logs"""
        return self._count_logs

    @staticmethod
    def clear_logs():
        """Clear logs in file"""
        with open(FILE_NAME, 'wb'):
            pass

    @staticmethod
    def read_logs():
        """func for get logs"""
        with open(FILE_NAME, "r+") as file:
            return file.readlines()

    @staticmethod
    def line_count():
        """get count lines in log file"""
        return sum(1 for _ in open(FILE_NAME))

    @staticmethod
    def check_logs(names):
        """Check logs by list names"""
        if os.stat(FILE_NAME).st_size == 0:
            return False

        with open(FILE_NAME, 'r') as file:
            last_line = file.readlines()[-1]
        reg = "\[(\w*)\:(\w*)\]"
        check = re.findall(reg, last_line)
        # check for current players (with restart)
        if [names] == check:
            return True
        return False

    @staticmethod
    def write_log_to_file(players, time, winner, wins):
        """Write info about players to log file"""
        count_win = wins[0] if winner == players[0] else wins[1]
        # two variants write log to file
        logging.basicConfig(filename=FILE_NAME, filemode='a', level=logging.DEBUG)
        if Logs.check_logs((players[0], players[1])):
            logging.debug(f' {time} - Winner: {winner}. Count wins: {count_win} - '
                          f'[{players[0]}:{players[1]}]')
        else:
            logging.debug(f' {time} - {winner} - [{players[0]}:{players[1]}]')
