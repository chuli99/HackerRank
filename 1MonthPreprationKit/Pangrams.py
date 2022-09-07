#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    s = s.replace(' ','')
    s = s.lower()
    i = 97 
    j = 0
    cont = 0
    abc = []
    while i <= 26:
        abc.append(chr(i))
        i += 1
        print(chr(i))
    print(abc)
    #if cont == 25:
    #    print('pangram')
    #else:
    #    print('not pangram')

string = 'We promptly judged antique ivory buckles for the next prize'
pangrams(string)