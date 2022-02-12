#!/bin/bash

echo -e "\nSort files by creation date:"
ls -al --sort=time
# in this command option: --sort=time responsible for sort...
# ...by time creating files
echo -e "\nAfter this files I can show u date and real time:"
date -u
# command date with option -u can show real time  UTC
echo ""
#it's like a \n for beauty :)
