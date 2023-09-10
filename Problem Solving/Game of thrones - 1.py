#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    set_s = list(set(s))
    count = 0
    for i in range(len(set_s)):
        occourrence_count = s.count(set_s[i])
        if occourrence_count % 2 != 0:
            count += 1
    
    if count > 1:
        return ("NO")
    else:
        return ("YES")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
