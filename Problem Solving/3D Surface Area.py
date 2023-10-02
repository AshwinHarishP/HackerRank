#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as a parameter.
#

def surfaceArea(A):
    # Write your code here
    x, y = len(A), len(A[0])
    Sum = 2 * x * y
    for i in range(x):
        for j in range(y):
            if i > 0:
                Sum += abs(A[i][j] - A[i-1][j])
            else:
                Sum += A[i][j]
            if j > 0:
                Sum += abs(A[i][j] - A[i][j-1])
            else:
                Sum += A[i][j]
            if i == x-1:
                Sum += A[i][j]
            if j == y-1:
                Sum += A[i][j]


    return Sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
