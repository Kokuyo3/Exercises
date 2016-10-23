#!/usr/bin/env python

#Textbook Exercise 2.4: Concat a list of lists - CT482
from arraylist import *

def listconcat(list):
		n = 0
		merge = arrayList()

		for i in range(0,list.END()):
			for j in range(0,list.elems[i].END()):
				merge.INSERT(list.elems[i].elems[j],n)
				n = (n+1)
		return merge