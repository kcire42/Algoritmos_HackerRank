#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive_values = 0 
    negative_values = 0
    zeros = 0
    length_arr = len(arr)
    for i in arr:
        #print(i)
        if i > 0:
            positive_values += 1
        elif i < 0:
            negative_values += 1
        else: 
            zeros += 1
    
    print(positive_values/length_arr)
    print(negative_values/length_arr)
    print(zeros/length_arr)


if __name__ == '__main__':
    #n = int(input().strip())

    #arr = list(map(int, input().rstrip().split()))
    n = 6
    arr = [-4,3,-9,0,4,1]
    plusMinus(arr)
