#!/usr/bin/env python

# Textbook Exercise 3.13:  Tree Conversion - CT482
# Takes a ____order list and converts that to a ____order list

class Tree():
    def __init__(self, elem=None, leftChild=None, rightChild=None):
        self.elem = elem
        self.leftChild = leftChild
        self.rightChild = rightChild

# A: Preorder listing of T into a postorder listing,
def pre_post(listing):
    temp = listing
    if len(listing) == 3: #If only one parent node and its two (L,R) children
        temp[0:2] = listing[1:3]
        temp[2] = listing[0]
        return temp
    else:
        temp = pre_post(listing[1:((len(listing) + 1) / 2)]) + pre_post(listing[((len(listing) + 1) / 2):]) + [listing[0]]
        return temp

# B: Postorder listing of T into a preorder listing,
def post_pre(listing):
    if len(listing) == 3:
        temp = listing
        temp[1:3] = listing[0:2]
        temp[0] = listing[2]
        return temp
    else:
        temp = [listing[-1]] + post_pre(listing[0: ((len(listing) - 1) / 2)]) + post_pre(listing[((len(listing) - 1) / 2): -1])
        return temp

# C: Preorder listing of T into a inorder listing,
def pre_in(listing):
    temp = listing
    if len(listing) == 3:
        t = temp[0]
        temp[0] = listing[1]
        temp[1] = t
        return temp
    else:
        temp = pre_in(listing[1: ((len(listing) + 1) / 2)]) + [listing[0]] + pre_in(listing[((len(listing) + 1) / 2):])
        # temp = pre_in( listing[ 0 : ( (len(listing)-1) /2) ] ) + [listing[ (len(listing)-1)/2 ]] + pre_in( listing[ ( (len(listing)+1) /2): ] )
        return temp