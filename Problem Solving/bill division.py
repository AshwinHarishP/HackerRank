#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    Sum = 0
    
    for items in range(len(bill)):
        
        if items == k:
            continue
        else:
            Sum += bill[items]
    
    Cost = int(Sum/2)
    
    if b == Cost:
        print("Bon Appetit")
    
    else:
        Actual_cost = b - Cost
        print(Actual_cost)
        
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
