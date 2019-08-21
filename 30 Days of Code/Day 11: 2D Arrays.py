#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))
sum = 0
max = -100
for i in range(0,4):
    for j in range(0,4):
        sum += arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if sum > max:
            max = sum
        sum = 0
print max
