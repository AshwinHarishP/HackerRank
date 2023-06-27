#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_position_count = 0
    orange_position_count = 0
    
    #Calculating apples land position list
    apple_position_list = []
    
    for apple_calc in range(len(apples)):
        apple_count = apples[apple_calc]+a
        apple_position_list.append(apple_count)

    
    #Calculating orange land position list
    orange_position_list = []
    
    for orange_calc in range(len(oranges)):
        orange_count = oranges[orange_calc]+b
        orange_position_list.append(orange_count)
    
    #Counting landing position of apple
    for apple_landing in apple_position_list:
        if apple_landing >= s and apple_landing <= t :
            apple_position_count += 1
    
    #Counting landing position of orange
    for orange_landing in orange_position_list:
        if orange_landing >= s and orange_landing <= t :
            orange_position_count += 1
    
    print(apple_position_count)
    print(orange_position_count)
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
