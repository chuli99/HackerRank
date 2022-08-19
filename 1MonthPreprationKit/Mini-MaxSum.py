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
    suMax = 0
    suMin = 0
    arr_sorted = sorted(arr)
    for i in range(len(arr_sorted)):
        if i >= 1:
            suMax += arr_sorted[i]
    for j in range(len(arr_sorted)):
        if j != len(arr_sorted)-1:
            suMin += arr_sorted[j]
    print(suMin,suMax)
#if __name__ == '__main__':

#    arr = list(map(int, input().rstrip().split()))

#    miniMaxSum(arr)

array = [1,2,3,4,5]

miniMaxSum(array)
