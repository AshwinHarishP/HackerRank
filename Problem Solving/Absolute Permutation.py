#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    if k == 0:
        return list(range(1, n + 1))
    
    if n % (2 * k) != 0:
        return [-1]
    
    used = [False] * (n + 1)
    permutation = []
    
    for i in range(1, n + 1):
        if i - k > 0 and not used[i - k]:
            permutation.append(i - k)
            used[i - k] = True
        else:
            permutation.append(i + k)
            used[i + k] = True
    
    return permutation



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
