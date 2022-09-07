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
<<<<<<< HEAD
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
=======
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
>>>>>>> 0004db53296e94f069154d875e6e658d91787fb0
