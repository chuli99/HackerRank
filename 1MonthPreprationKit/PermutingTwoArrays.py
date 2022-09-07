#!/bin/python3

import math
import os
import random
import re
import sys
from traceback import print_tb

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k,A, B):
    A = sorted(A)
    B = sorted(B)
    B.reverse()
    
    cont = 0
    for i in range(len(A)):
        if (A[i] + B[i]) >= k:
            cont += 1
    if cont == len(A):
        print('YES')
    else:
        print('NO')

""" 
if __name__ == '__main__':
    fptr = open('D:/CURSOS/HackerRank/HackerRank/1MonthPreprationKit/sexo.txt', 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
"""
