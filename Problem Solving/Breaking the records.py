#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    lowest_score_beats = 0
    highest_score_beats = 0
    
    highest_score = scores[0]
    lowest_score = scores[0]
    
    #For finding highest score
    for i in range(1,len(scores)):
        if scores[i] > highest_score:
            highest_score_beats += 1
            highest_score = scores[i] 
    
    #For finding lowest_score
        if scores[i] < lowest_score:
            
            lowest_score = scores[i]
            lowest_score_beats += 1
                
    return [highest_score_beats , lowest_score_beats]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
