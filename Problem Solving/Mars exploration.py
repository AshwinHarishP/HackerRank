#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    count = 0
    sos_count = int(len(s)/3)
    orginal_sos = sos_count*"SOS"
    
    for letters in range(len(orginal_sos)):
        if orginal_sos[letters] != s[letters]:
            count += 1
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
