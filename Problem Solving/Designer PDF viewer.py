#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    
    #getting index of letters in word 
    character_list = []
    for i in range (len(word)):
        element = (ord(word[i]) - 97)
        character_list.append(element)
    
    #getting numbers from h using calculated index    
    index_list = []
    for elements in character_list:
        index_list.append(h[elements])
    
    #Calculating maximum and legth from calculated h    
    maximum_element = max(index_list)
    length = len(index_list)
    
    #Finding area using maximum and length
    area = maximum_element*length
    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
