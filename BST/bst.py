#!/usr/bin/env python

# Problem 3 - Binary Search Tree Dictionary - CT482

class CellType:
    def __init__(self, elem=None, leftChild=None, rightChild=None):
        self.elem = elem
        self.leftChild = leftChild
        self.rightChild = rightChild

    def __str__(self):
        return str(self.elem)


# MEMBER
def MEMBER(x, A):
    if A == None:
        return False
    elif x == A.elem:
        return True
    elif x < A.elem:
        return MEMBER(x, A.leftChild)
    elif x > A.elem:
        return MEMBER(x, A.rightChild)


# INSERT
def INSERT(x, A):
    if A == None:
        A = CellType(x)
        A.leftChild = None
        A.rightChild = None
    elif x < A.elem:
        if A.leftChild != None:
            INSERT(x, A.leftChild)
        else:
            A.leftChild = CellType(x)
    elif x > A.elem:
        if A.rightChild != None:
            INSERT(x, A.rightChild)
        else:
            A.rightChild = CellType(x)
    return A


# DELETEMIN
def DELETEMIN(A):
    if A.leftChild == None:
        A = A.rightChild
        return A.elem
    else:
        return DELETEMIN(A.leftChild)


# DELETE
def DELETE(x, A):
    if A != None:
        if x < A.elem:
            DELETE(x, A.leftChild)
        elif x > A.elem:
            DELETE(x, A.rightChild)
        elif ((A.leftChild == None) and (A.rightChild == None)):
            A = None
        elif A.leftChild == None:
            A = A.rightChild
        elif A.rightChild == None:
            A = A.leftChild
        else:
            A.elem = DELETEMIN(A.rightChild)


# LOCATE
def LOCATE(x, A, i=0):
    if A == None:
        return None
    elif x == A.elem:
        return i
    elif x < A.elem:
        return LOCATE(x, A.leftChild, i + 1)
    elif x > A.elem:
        return LOCATE(x, A.rightChild, i + 1)
