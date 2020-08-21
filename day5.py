#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    num = int(input())
    for count in range (0, 10):
        print(f'{num} x {count + 1} = {num * (count + 1)}\n')


