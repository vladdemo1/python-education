"""In this task I will work with lists"""
names = ["Vlad", ["John", "Adam"]]
numbers = [n**2 for n in range(1, 11)]
strings = [letter for letter in names[1][1]]

print(*numbers)    # list numbers
print(names[1][0][:2])    # Jo
