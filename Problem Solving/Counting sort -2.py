#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 101

    # Store the count of each element in the count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cumulative count
    for i in range(1, 101):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # Place the elements in the output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into the original array
    for i in range(0, size):
        array[i] = output[i]
    return array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    array = list(map(int, input().rstrip().split()))

    result = countingSort(array)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
