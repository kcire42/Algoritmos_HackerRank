#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    primary_diagonal = 0 
    secondary_diagonal = 0

    
    # print(len(arr))
    # for i in range(len(arr)):
    #     print(arr[i])
    for i in range(0, len(arr)):
        #print(arr[i][i])
        primary_diagonal += arr[i][i]
        secondary_diagonal += arr[len(arr)-i-1][i]
        #print(i)
        #print(len(arr)-i-1)
        #print(arr[len(arr)-i-1][i])
    # for i in range(0,len(arr)):
    #     print(arr[i])
    return abs(primary_diagonal-secondary_diagonal)

if __name__ == '__main__':

    # n = int(input())

    # arr = []

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))
    arr = [[1,2,3],[4,5,6],[7,8,9]]

    result = diagonalDifference(arr)
    


