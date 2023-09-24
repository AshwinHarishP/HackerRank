import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    
    if len(a) == 1:
        return a[0]
    
    count_arr = Counter(a)
    print(count_arr)
    value_list = []
    
    for key, values in count_arr.items():
        value_list.append(values)
        
    value_list.sort()

    if (value_list[0] != value_list[1]):
        lonely = value_list[0]
    
    for key, value in count_arr.items():
        if value == lonely:
            return key

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
