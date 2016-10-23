#!/usr/bin/env python

#Textbook Exercise 3.10: Level-order listing of tree nodes - CT482

class tree():
    def __init__(self,cSpace = None):
        self.cSpace = cSpace
        self.child = []

    def newChild(self,c):
        self.child.append(c)

def levelorder(T):
    A = []
    A.append(T)
    B = []
    B.append(T)
    
    while A:
        temp = A.pop(0)
        for elem in temp.child:
            x = elem
            if x not in B:
                A.append(x)
                B.append(x)
    return B