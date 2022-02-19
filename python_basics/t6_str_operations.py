"""Task about basics string operations"""
s = "Hey thera! what sho?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("In text a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:6])   # Start to 5 id
print("The next five characters are '%s'" % s[5:11])   # 5 to 10
print("The thirteenth character is '%s'" % s[11])   # Just number 12
print("The characters with odd index are '%s'" % s[1::2])
print("The last five characters are '%s'" % s[-5:])   # 5th-from-last to end

# Convert everything to uppercase
text = "String in uppercase: "
print(f"{text.upper()}{s.upper()}")

# Convert everything to lowercase
lower = "String in lowercase: "
print(f"{lower.lower()}{s.lower()}")

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("sho?"):
    print("String ends with 'sho?'. Good!")

# Split the string into four separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
