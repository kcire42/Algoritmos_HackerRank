#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    max = sum(arr[1::])
    min = sum(arr[0:4])
    print(f"{min} {max}")



if __name__ == '__main__':

    #arr = list(map(int, input().rstrip().split()))
    arr = [5,4,3,2,1]
    miniMaxSum(arr)