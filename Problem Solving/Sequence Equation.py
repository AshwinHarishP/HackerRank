#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    n = max(p)
    dict_ele = dict()
    result = []
    for i in range(1,n+1):
        dict_ele[i] = p[i-1]        
    
    for i in range(1,n+1):
        for key,value in dict_ele.items():
            if value == i:
                temp = key
        for key,value in dict_ele.items():
            if value == temp:
                result.append(str(key))
    
    for i in result:
        return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
