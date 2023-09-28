#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    max_distance = 0
    last_space = -1
    
    for station in c:
        if last_space == -1:
            max_distance = station
        else:
            distance = (station - last_space) // 2
            max_distance = max(max_distance, distance)
        last_space = station
        
    max_distance = max(max_distance, n-1 - last_space)
    return max_distance
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
