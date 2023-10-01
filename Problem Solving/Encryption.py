#!/bin/python3

from math import *
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    l = len(s)
    row = floor(sqrt(l))
    col = ceil(sqrt(l))
    result = []
    for i in range(col):
        temp = []        
        j = 0
        while(i + j < l):
            temp.append(s[i + j])
            j += col
        
        result.append("".join(temp) + " ")
        print(result)
        
    return "".join(result)
            
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
