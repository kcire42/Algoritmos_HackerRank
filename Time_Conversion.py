#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    splitlist = s.split(":")
    hour,min,sec,period = int(splitlist[0]),str(splitlist[1]),str(splitlist[2][0:2]),str(splitlist[2][2:4])
    if period.endswith("PM") and hour != 12:
        hour = hour+12
        time = str(hour)+":"+min+":"+sec
        return time
    elif period.endswith("AM") and hour != 12:
        if hour > 9:
            time = str(hour)+":"+min+":"+sec
            return time
        else:
            time = "0"+str(hour)+":"+min+":"+sec
            return time

    elif period.endswith("PM") and hour == 12:
        time = str(hour)+":"+min+":"+sec
        return time
    elif period.endswith("AM") and hour == 12:
        hour = "00"
        time = hour+":"+min+":"+sec
        return time

if __name__ == '__main__':
    s = "07:05:45PM"
    result = timeConversion(s)
    print(result)
    s1 = "06:40:03AM"
    result1 = timeConversion(s1)
    print(result1)
    s2 = "08:40:03AM"
    result2 = timeConversion(s2)
    print(result2)
    s3 = "11:40:03AM"
    result3 = timeConversion(s3)
    print(result3)


   