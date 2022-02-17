"""In this task I need assign to vars some values"""
message = "hello"
weight = 10.0
price = 20

# main code
if len(message) == 5:
    print(message[::-1])
else:
    print(message[::4]*3)   # hohoho
if isinstance(weight, float) and isinstance(price, int):
    print(f"Float -> {weight} and Int -> {price}")

letters = [letter for letter in [*message] if letter < "l"]
print(*letters, sep='')   # print letters which less 'l'
