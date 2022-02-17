"""Task about something operators + lists"""
first_list = [n for n in range(1, 4)]*3
second_list = [5, 6, 7]*2
big_list = first_list + second_list
# Print all lists
print(*first_list)
print(*second_list)
print(*sorted(big_list))    # sorted all lists
