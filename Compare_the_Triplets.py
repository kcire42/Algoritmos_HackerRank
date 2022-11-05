import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    points_alice = 0
    points_bob = 0 
    for i in range(len(a)):
        if a[i] > b[i]:
            #print("punto alice")
            points_alice += 1
        elif a[i] < b[i]:
            #print("punto bob")
            points_bob += 1
        else:
            continue
    # print(f"Puntos de alice: {points_alice}")
    # print(f"Puntos de bob: {points_bob}")
    return [points_alice,points_bob]
        

if __name__ == '__main__':

    # a = list(map(int, input().rstrip().split()))

    # b = list(map(int, input().rstrip().split()))
    b = [1,2,3]
    a = [4,5,6]
    result = compareTriplets(a, b)
