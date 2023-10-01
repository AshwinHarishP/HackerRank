#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    sorted_grid = []
    for i in grid:
        sorted_grid.append("".join(sorted(i)))
    
    sorted_grid = "".join(sorted_grid)
    col = []
    sorted_col = []
    
    for i in range(n):
        j = 0
        char = ""
        
        while i + j < len(sorted_grid):
            char += sorted_grid[i+j]
            j += n
        col.append(char)
        sorted_col.append("".join(sorted(char)))
        
    if col == sorted_col:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
