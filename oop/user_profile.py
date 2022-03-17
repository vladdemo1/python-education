"""Class about user profile"""


class UserProfile:
    """Class User contain all functions about profile"""
    def __init__(self, number=0, name="Client"):
        self.number = number
        self.name = name

    @staticmethod
    def info():
        """Func info say about this class"""
        print("This class contain information about profile user's")

    def get_info_user(self):
        """This func returned number and then name of user"""
        return self.number, self.name
