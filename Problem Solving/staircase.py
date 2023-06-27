#!/bin/python3

import math
import os
import random
import re
import sys



def staircase(n):
    for rows in range(1,n+1):
        left_space = " "*(n-rows)
        hashes = "#"*rows
        print(left_space+hashes)


if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
