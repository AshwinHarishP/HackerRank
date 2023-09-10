#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    count_values = Counter(s)
    count_list = []
    
    #appending count value in list
    for key,value in count_values.items():
        count_list.append(value)
    
    count_list = sorted(count_list)
    
    #Case1: Checking all elements are same
    if len(set(count_list)) == 1:
        return "YES"
    
    #Case2: More than 2 unique frequencies
    elif len(set(count_list)) > 2:
        return "NO"
    
    #Case3: 
    else:
        for key in count_values:
            count_values[key] -= 1
            temp = list(count_values.values())
            try:
                temp.remove(0)
            except:
                pass
            
            if len(set(temp)) == 1:
                return "YES"
            else:
                count_values[key] += 1
        return "NO"
        
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
