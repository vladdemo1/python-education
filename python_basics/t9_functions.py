"""Task about functions"""


def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse",
            "Allowing programmers to share and connect code together"]


# return string where word + is a ...
def build_sentence(benefit):
    return f"{benefit} - is a benefit of functions!"


# this func print all list
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


# edit the functions prototype and implementation
def foo(a: int, b: int, c: int, *args: int):
    if len(args) > 0:
        if a + b + c == args[0]:
            return 1
    return False


def bar(a, b, c, **numbers):
    if numbers.get('magicnumber') == 6:
        return False
    elif numbers.get('magicnumber') == 7:
        return True
    return [a, b, c]


def func_args():
    # test code
    if foo(1, 2, 3, 6) == 1:
        print("Good.")
    if foo(1, 2, 3, 4, 5) == 2:
        print("Better.")
    if not bar(1, 2, 3, magicnumber=6):
        print("Great.")
    if bar(1, 2, 3, magicnumber=7):
        print("Awesome!")


if __name__ == "__main__":
    name_the_benefits_of_functions()
    func_args()
