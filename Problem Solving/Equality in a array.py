#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from collections import Counter
def equalizeArray(arr):
    count_list = []
    count_arr = Counter(arr)
    
    for key,value in count_arr.items():
        count_list.append(value)
        
    count_list.remove(max(count_list))
    
    Sum = 0
    for i in count_list:
        Sum += i
    return Sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
