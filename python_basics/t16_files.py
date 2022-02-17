"""Task about files"""

# just open something file
f = open('t12_sets.py', 'r')
# print all text in file t12_sets.py
print(f.read())

# print text to file text.txt
new_file = open('text.txt', 'w')
new_file.write("Added something text to this file!")
