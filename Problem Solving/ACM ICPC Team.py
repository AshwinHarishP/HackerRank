#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    max_topics = 0
    max_team_known = 0
    
    for i in combinations(topic, 2):
        number1, number2 = i
        
        value = bin(int(number1, 2) | int(number2, 2)).count("1")
        
        if value > max_topics:
            max_topics = value
            max_team_known = 1
        
        elif value == max_topics:
            max_team_known += 1
            
    return max_topics, max_team_known
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
