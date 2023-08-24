#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    n = str(n)
    d = []
    
    for elements in n:
        digits = int(elements)
        d.append(digits)
    
    n = int(n)
    count = 0
    
    for i in range(len(d)):
        
        if d[i] != 0:
            divisible = n%d[i]
            
        elif d[i] == 0:
            continue
            
        if divisible == 0:
            count += 1
    
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
