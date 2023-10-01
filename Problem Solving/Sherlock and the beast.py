#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    if n in [1, 2, 4, 7]:
        print('-1')
    else:
        i = 0
        while n % 3 != 0:
            n -= 5
            i += 5
        print('5' * n + '3' * i)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
