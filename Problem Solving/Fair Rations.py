#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    trans = 0
    for i in range(len(B)-1):
        if B[i] % 2 == 1:
            B[i] += 1
            B[i+1] += 1
            trans += 2
            
    for j in B:
        if j % 2 == 1:
            return "NO"
    else:
        return str(trans)        
             

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
