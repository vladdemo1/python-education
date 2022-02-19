"""Task about imports"""

from math import sqrt as q

first, second = [int(input()) for _ in range(2)]
# in this situation q - it's a sqrt
if first**2 == q(second):
    print("First^2 == sqrt(second)")
else:
    print("Wrong")
