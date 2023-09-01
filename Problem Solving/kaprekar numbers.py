#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    elements = []
    for i in range(p,q+1):
        n = i**2
        d = int(len(str(i)))
        left_part = n//(10**d)
        right_part = n%(10**d)
        if left_part+right_part == i:
            elements.append(i)
    
    if len(elements) == 0:
        print("INVALID RANGE") 
    
    else:
        print(*elements) 

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
