#!/usr/bin/env python

#-----List: listconcat test - CT482
from listconcat import *

print("Make a list, A.")
A = arrayList()

for i in range(0,5) :
    B = arrayList()
    for j in range(0,5):
        B.INSERT((i+1)*j,j)
    A.INSERT(B,i)

for i in range(0,len(A.elems)):
    print ("List A[" + str(i) + "] = " + str(A.elems[i].elems))

print("After listconcat(): " + str(listconcat(A).elems))


