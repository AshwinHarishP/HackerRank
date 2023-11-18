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
    weights = set()  # Use a set to store the weighted uniform values

    prev_char = None
    weight = 0

    for char in s:
        if char == prev_char:
            weight += (ord(char) - 96)
        else:
            weight = (ord(char) - 96)
            prev_char = char

        weights.add(weight)

    results = []
    for query in queries:
        if query in weights:
            results.append("Yes")
        else:
            results.append("No")

    return results


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
