#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()
    l = 0
    r = 1
    max_count = 0
    
    while r < len(a):
        if abs(a[r] - a[l]) <= 1:
            max_count = max(max_count, (r - l) + 1)
            r += 1
        else:
            l += 1
            r = l + 1
    
    return max_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
