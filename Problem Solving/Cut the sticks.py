#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    length = len(arr)
    count = [length]
    
    while len(arr) > 1:
        shortest = min(arr)
        arr = list(filter(lambda x: x!=shortest,arr))
        
        for i in range(len(arr)):
            arr[i] = arr[i] - shortest
        
        if len(arr)>0:
            count.append(len(arr))
    
    for _ in range(len(count)):
        return(count)
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
