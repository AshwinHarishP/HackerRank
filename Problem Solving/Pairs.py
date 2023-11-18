#!/bin/python3

import math
import os
import random
import re
import sys

def pairs(k, arr):
    arr.sort()
    count = 0
    left = 0
    right = 1

    while right < len(arr):
        diff = arr[right] - arr[left]

        if diff == k:
            count += 1
            right += 1
        elif diff < k:
            right += 1
        else:
            left += 1

            if left == right:
                right += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
