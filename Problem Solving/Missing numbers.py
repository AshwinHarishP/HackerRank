#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    
    dict_a = {}
    dict_b = {}
    lack_element_list = []
    
    for i in range(len(arr)):
        dict_a[arr[i]] = arr.count(arr[i])
        
    for j in range(len(brr)):
        dict_b[brr[j]] = brr.count(brr[j])
        
    for key,value in dict_b.items():
        if value != dict_a.get(key,0):
            lack_element_list.append(key)
    
    return (sorted(lack_element_list))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
