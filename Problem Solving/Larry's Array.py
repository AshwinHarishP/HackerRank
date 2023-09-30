#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    inventions = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                inventions += 1
    if inventions % 2 == 1:
        return "NO"
    return "YES"
            
    return str(10000)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
