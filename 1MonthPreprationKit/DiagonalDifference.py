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
    sum = 0
    sum2 = 0
    cont = 0
    for i in range(len(arr)):
        sum += ((arr[i])[i])        
        cont -= 1
        sum2 +=((arr[cont])[i])
    
    return(abs(sum-sum2))
        

"""
[11, 2, 4], 
[4, 5, 6], 
[10, 8, -12]]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
"""


array = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
diagonalDifference(array)