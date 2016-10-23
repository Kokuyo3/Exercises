#!/usr/bin/env python

# Problem 3 - Binary Search Tree Dictionary: Test - CT482

from bst import *
from math import *
from random import *

nLoops = 30
sumLen = 0

listLen = []
listAvg = []

for i in range(1, nLoops + 1):
    BST = None

    maxVal = 10 * i
    vals = range(0, maxVal)
    shuffle(vals)

    for j in vals:
        BST = INSERT(j, BST)
        sumLen += LOCATE(j, BST)

    listAvg.append(float(sumLen) / float(maxVal))

print("n \t| O(log_2(n)) \t\t| Average Length")
print("-" * 50)
for i in range(nLoops):
    print((i + 1) * 10, log((i + 1) * 10, 2), listAvg[i])

