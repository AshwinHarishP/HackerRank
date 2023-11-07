#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr,l,r):
    if l < r:
        pivot = arr[l]
        i = l
        j = r
        while i < j:
            i += 1
            while i <= r and arr[i] < pivot:
                i += 1
            while j >= 1 and arr[j] > pivot:
                j -= 1
            
            if i < j and i <= r:
                arr[i],arr[j] = arr[j],arr[i]
        
        arr[l],arr[j] = arr[j],arr[l]
        quickSort(arr, 0, j-1)
        
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr,0,len(arr)-1)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
