#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles:list)->int:
    # Write your code here
    candles.sort(reverse=True)
    count = 0
    for i in candles:
        if candles[0] == i:
            count +=1
    return count

if __name__ == '__main__':
    #candles_count = int(input().strip())
    #candles = list(map(int, input().rstrip().split()))
    candles_count = 4
    candles = [3, 2, 1, 3]
    result = birthdayCakeCandles(candles)
    print(result)

    
