#!/bin/python3

import math
import os
import random
import re
import sys


def simpleArraySum(ar):
    Sum = 0
    for i in range(len(ar)):
        Sum+=ar[i]
    return Sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
