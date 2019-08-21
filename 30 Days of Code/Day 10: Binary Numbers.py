#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input())
    nums = []
    while n>0:
        nums.append(n%2)
        n = n //2
    cont = 0
    sol = 0
    for i in nums:
        
        if i == 1:
            cont+= 1
            if cont > sol:
                sol = cont
        else:
            cont = 0
    print sol


