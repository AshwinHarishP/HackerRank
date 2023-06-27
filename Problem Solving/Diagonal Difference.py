#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    left_diagonal = 0
    right_diagonal = 0
    diagonal = abs(n-(n+1))
    
    for i in range(len(arr)):
        for j in range(diagonal):
            left_diagonal += arr[i][i]
    i=0
    j=0    
    k = len(arr)-1
    
    for i in range(len(arr)):
        for j in range(diagonal):
            right_diagonal += (arr[i][k])
        k -= 1
    difference = abs(int(right_diagonal) - int(left_diagonal))
    return(str(difference))
    
    
             

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
