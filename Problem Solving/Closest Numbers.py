#!/bin/python3

import math
import os
import random
import re
import sys

def closestNumbers(arr):
    arr = sorted(arr)
    minimum_diff = float('inf')
    diff_list = []

    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if diff < minimum_diff:
            minimum_diff = diff
            diff_list = [arr[i], arr[i + 1]]
        elif diff == minimum_diff:
            diff_list.extend([arr[i], arr[i + 1]])

    # Return the list directly without using join
    return diff_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    # Format the output as a space-separated string
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
