"""Task about important python modules: time, datetime, os and sys"""

from datetime import time, datetime
from os import name

print(name)   # printed 'posix'

start_time = datetime.now()   # time started
# In this place running some functions
temp = 0
for i in range(50000):
    temp += i
print(datetime.now() - start_time)

# print all func time
print(dir(time))
# print date now
print(datetime.now())
