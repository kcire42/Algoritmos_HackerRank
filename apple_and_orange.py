#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(point_s_house, point_t_house, position_tree_apples, position_tree_oranges, apples, oranges):
    # Write your code here
    array_apples = []
    for apple in apples:
        array_apples.append(position_tree_apples+apple)
    array_oranges = []
    for orange in oranges:
        array_oranges.append(position_tree_oranges+orange)
    print(array_apples)
    print(array_oranges)
    apples_house = 0
    for i in array_apples:
        if i >= point_s_house and i <= point_t_house:
            apples_house += 1
    oranges_house = 0
    for j in array_oranges:
        if j >= point_s_house and j <= point_t_house:
            oranges_house += 1
    print(apples_house)
    print(oranges_house)
    
    

if __name__ == '__main__':
    #Distancia de casa de s a t
    # first_multiple_input = input().rstrip().split()

    # point_s_house = int(first_multiple_input[0])

    # point_t_house = int(first_multiple_input[1])
    # #Distancia de los arboles
    # second_multiple_input = input().rstrip().split()

    # tree_apples = int(second_multiple_input[0])

    # tree_oranges = int(second_multiple_input[1])
    # #Cantidad de manzanas y naranjas
    # third_multiple_input = input().rstrip().split()

    # quantity_apples = int(third_multiple_input[0])

    # quantity_oranges = int(third_multiple_input[1])
    # #Distancias de manzanas y naranjas
    # apples = list(map(int, input().rstrip().split()))

    # oranges = list(map(int, input().rstrip().split()))
    point_s_house = 7
    point_t_house = 10
    position_tree_apples = 4
    position_tree_oranges = 12
    apples = [2,3,-4]
    oranges = [3,-2,-4]
    countApplesAndOranges(point_s_house, point_t_house, position_tree_apples, position_tree_oranges, apples, oranges)
