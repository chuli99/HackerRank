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
    countpositive = 0
    countzeros = 0
    countnegative = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > 0:
            countpositive += 1
        elif arr[i] == 0:
            countzeros += 1
        else:
            countnegative += 1
    print(countpositive/n)
    print(countnegative/n)
    print(countzeros/n)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

