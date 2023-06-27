#!/bin/python3

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    element_list = []
    k = -1
    index = len(arr)
    
    for i in range(index):
        
        if index + k > index:
            element = sum(arr[i:] + arr[:k])
            element_list.append(element)
            k += 1

        
        else:
            element = sum(arr[i:index+k])
            element_list.append(element)
            k += 1
            
    print(str(min(element_list))+ " " +str(max(element_list)))
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
