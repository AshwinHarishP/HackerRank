#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    cipher = ""
    temp = 0
    for i in range(len(s)):
        temp = ord(s[i])
        if s[i].islower():
            temp -= 97
            temp += k
            temp %= 26
            temp += 97
        elif s[i].isupper():
            temp -= 65
            temp += k
            temp %= 26
            temp += 65
        cipher += str(chr(temp))
    return(cipher)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
