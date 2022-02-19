"""Task about modules and packages"""

import re

# added to list all func from re then contains 'find'
find_members = [func for func in dir(re) if "find" in func.lower()]
print(sorted(find_members))   # this print show 'findall' and 'finditer'
