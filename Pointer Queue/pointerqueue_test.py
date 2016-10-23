#!/usr/bin/env python

#-----Queue: Pointer Testing - CT482
from pointerqueue import *

Q = pointerqueue()
print("Initialized queue.")
print("Is the queue empty: " + str(Q.EMPTY()))

print("Running a few ENQUEUE() calls")
Q.ENQUEUE(1)
Q.ENQUEUE(3)
Q.ENQUEUE(5)
Q.ENQUEUE(7)
Q.ENQUEUE(9)
Q.ENQUEUE(11)

print("After ENQUEUE() runs: " + Q.PRINTQ())
print("Is the queue empty: " + str(Q.EMPTY()))

print("Running DEQUEUE()")
Q.DEQUEUE()
print("After 1x DEQUEUE(): " + Q.PRINTQ())
Q.DEQUEUE()
print("After 2x DEQUEUE(): " + Q.PRINTQ())

print("Front element: " + str(Q.FRONT()))

print("Calling MAKENULL()...")
Q.MAKENULL()
print("Is the queue empty: " + str(Q.EMPTY()))