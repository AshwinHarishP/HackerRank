#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    negative_count = 0
    possitive_count = 0
    zero_count = 0
    length = len(arr)
    for elements in range(len(arr)):
        if arr[elements] < 0:
            negative_count+=1
        elif arr[elements] > 0:
            possitive_count+=1
        elif arr[elements] == 0:
            zero_count+=1
    possitive = (possitive_count/length)
    possitive_number = "{:.6f}".format(possitive)

    negative = (negative_count/length)
    negative_number = "{:.6f}".format(negative)
    zero = (zero_count/length)
    zero_number = "{:.6f}".format(zero)
    
    
    print(possitive_number)
    print(negative_number)
    print(zero_number)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
