import math as M
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    x = meal_cost + meal_cost*tip_percent/100 + meal_cost*tax_percent/100
    if(x * 10 - int(x)*10 >=5):
        print(M.ceil(x))
    else:
        print(M.floor(x))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())
    
    solve(meal_cost, tip_percent, tax_percent)
