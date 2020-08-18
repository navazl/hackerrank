import math
import os
import random
import re
import sys


# Complete the solve function below.

def solve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost * (tip_percent/100))
    tax = (meal_cost * (tax_percent/100))
    totalCost = meal_cost + tip + tax
    return round(totalCost)
       


if __name__ == '__main__':
    meal = float(input())
    tipP = int(input())
    taxP = int(input())
    print(solve(meal, tipP, taxP))

