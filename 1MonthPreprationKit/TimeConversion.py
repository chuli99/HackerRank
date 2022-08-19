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
    ns = ''
    #Condicion para cambiar formato AM
    if (s[-2:].upper()) == 'AM':
        #Condicion para cambiar las 12hs en pm y am
        if s[:2] == '12':
            s = s.replace('12','00')
        ns = s.replace('AM','')
        print(ns)
    #Condicion para cambiar formato PM
    if (s[-2:].upper()) == 'PM':
        #Condicion para cambiar las 12hs en pm y am
        if s[:2] == '12':
            s = s.replace('12','00')
        
        s = s.replace('PM','')
        #Primeros 2 caracteres
        firstcar = s[:2]
        sum = int(firstcar) + 12
        #nueva hora
        ns = s.replace(firstcar,str(sum))
        print(ns)

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

#    s = input()

#    result = timeConversion(s)

#    fptr.write(result + '\n')

#    fptr.close()

time = str('12:05:45PM')
timeConversion(time)