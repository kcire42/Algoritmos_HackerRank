#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    grades_round = []
    for grade in grades:
        if grade >= 38 and grade%5 >=3:
            grades_round.append(grade-(grade%5)+5)
            
        else:
            grades_round.append(grade)
    return grades_round
if __name__ == '__main__':
    # grades_count = int(input().strip())

    # grades = []

    # for _ in range(grades_count):
    #     grades_item = int(input().strip())
    #     grades.append(grades_item)
    grades = [73,67,38,33]

    result = gradingStudents(grades)
    print(result)
