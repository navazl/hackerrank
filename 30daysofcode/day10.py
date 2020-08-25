#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binario = bin(n)[2:].split('0')
    print(len(max(binario)))