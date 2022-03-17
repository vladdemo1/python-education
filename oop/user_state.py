"""Class UserState with states for user"""


class UserState:
    """This class's have a many states for user"""

    states = ("New", "Active", "Blocked", "Banned")

    @staticmethod
    def show_states():
        """This func show's all states"""
        print(UserState.states)

    @staticmethod
    def info():
        """Main info about class"""
        print("This class needed to contain states")


if __name__ == "__main__":
    UserState.info()
    UserState.show_states()
