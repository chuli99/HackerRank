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
    abc = [chr(index) for index in range(97,123)]
    s = s.replace(' ','')
    ns = [str.lower(s[i]) for i in range(len(s))]
    print(ns)
    cont = 0
    for i in abc:
        for j in ns:
            if i == j:
                cont += 1
                break
    print(cont)
    if cont == 26:
        return('pangram')
    else:
        return('not pangram')

str1 = "We promptly judged antique ivory buckles for the prize"
str2 = "We promptly judged antique ivory buckles for the next prize"
pangrams(str2)
