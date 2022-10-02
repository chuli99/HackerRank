#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    binario = list('{:032b}'.format(n))
    for index in range(len(binario)):
        if binario[index] == '1':
            binario[index] = '0'
        else:
            binario[index] = '1'
    return int(''.join(binario),2)

arr = [2147483647,1,0]
print(arr[0])
for i in arr:
    flippingBits(i)
    
nro = str('00000000000000000000000000000011')
#flippingBits(nro)