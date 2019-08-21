#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
cont = 0
for i in range(n):
    swaps = 0
    
    for j in range(n-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            swaps+=1
            cont+=1
    if swaps == 0:
        break
print("Array is sorted in "+ str(cont) + " swaps.\n" + "First Element: " + str(a[0])+"\n"+"Last Element: " + str(a[len(a)-1]))
