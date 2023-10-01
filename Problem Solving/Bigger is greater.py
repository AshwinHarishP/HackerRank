#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(s):
    
    s = list(s)
    
    
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i+1]:
        i -= 1
    
    
    if i == -1:
        return "no answer"
    
    
    j = len(s) - 1
    while s[j] <= s[i]:
        j -= 1
    
    s[i], s[j] = s[j], s[i]
    
    
    s[i+1:] = reversed(s[i+1:])
    
    
    return ''.join(s)



    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
