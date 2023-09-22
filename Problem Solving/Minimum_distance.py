#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    count_arr = Counter(a)
    res = list()
    flag = False
    for key, value in count_arr.items():
        if value > 1:
            flag = True
            index = list()
            
            for i in range(len(a)):
                if a[i] == key:
                    index.append(i)
            res.append(abs(index[0] - index[1]))
            
    if flag == False:
        return -1
    
    return (min(res))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
