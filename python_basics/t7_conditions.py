"""Task about conditions"""

number = 10
second_number = 10
first_array = []
second_array = [1, 2, 3]

if number*2 > 15:
    print("1")

if len(first_array) == 0:
    print("2")

second_array.append(4)
if second_array[1] == 2:
    print("3")

first_array.append(1)
if len(first_array) + len(second_array) == 5:
    print("4")

if len(first_array) and first_array[0] == 1:
    print("5")

if second_number > len(second_array):
    print("6")
