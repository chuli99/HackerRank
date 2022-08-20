#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    for i in a:
        count = 0
        for j in a:
            if i == j:
                count += 1
        if count == 1:
            return(i)

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

#    n = int(input().strip())

#    a = list(map(int, input().rstrip().split()))

#    result = lonelyinteger(a)

#    fptr.write(str(result) + '\n')

#    fptr.close()


arr = [63,25,73,1,98,73,56,84,86,57,16,83,8,25,81,56,9,53,98,67,99,12,83,89,80,91,39,86,76,85,74,39,25,90,59,10,94,32,44,3,4,8,7,3,7,9,2,8,3,7,9,2,21,92,69,81,40,40,34,68,78,24,87,42,69,23,41,78,22,6,90,99,89,50,30,20,1,43,3,70,95,33,46,44,9,69,48,33,60,65,16,82,67,61,32,21,79,75,75,13,87,70,33]
lonelyinteger(arr)