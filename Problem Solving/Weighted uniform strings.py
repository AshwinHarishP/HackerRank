#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    List = []
    element = -1
    while element < len(s) -1:
        element += 1
        digit  = ord(s[element])-96
        List.append(digit)
        
        while element < len(s)-1 and s[element+1] == s[element]:
            digit  += ord(s[element])-96
            List.append(digit)
            element += 1
    
    Result = []
    for querry in queries:
        if querry in List:
            Result.append("Yes")
        else:
            Result.append("No")
    
    return Result
            
        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
