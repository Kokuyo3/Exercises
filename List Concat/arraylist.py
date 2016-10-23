#!/usr/bin/env python

#List: Array Implementation - CT482

maxLen = 1000 #Max nodes

class arrayList:
    def __init__(self,i_Last = -1):
        self.elems = []
        self.end = i_Last
        return

#FIRST
    def FIRST(self):
        if self.end >= 0:
            return 0
        else:
            return -1

#END
    def END(self): #END(L) will return the position following position n in an n-element list L
        return self.end + 1

#RETRIEVE
    def RETRIEVE(self,p): #Returns the element at position p on list L.
        if p <= self.END() and p >= 0:
            return self.elems[p]
        else:
            print "Index out of bounds"

#LOCATE
    def LOCATE(self,x):
        for i in range(0,self.END()):
            if self.elems[i] == x:
                return i
            else:
                return self.END()

#NEXT
    def NEXT(self,p):
         if p > self.END():
             print "Index out of bounds"
         else:
             return (p+1)

#PREVIOUS
    def PREVIOUS(self,p):
        if p > -1:
            return (p-1)
        else:
            return -1

#INSERT
    def INSERT(self,x,p):
        if p > self.END() or (p < 0):
            print "Index out of bounds"
        elif self.end >= maxLen:
            print "Full list"
        else:
            self.elems.insert(p,x)
            self.end = self.end + 1

#DELETE
    def DELETE(self,p):
        if p <= self.end and p >= 0:
            self.end = self.end - 1
            self.elems.pop(p)
            return
        else:
            print "Index out of bounds"

#MAKENULL
    def MAKENULL(self):
        return self.__init__(i_Last = -1)

#PRINTL
    def PRINTL(self):
        out = ""
        if list != None:
            for i in range(0,len(self.elems)):
                out = (out + str(self.elems[i]) + ", ")
            print out
        else:
            print("List is empty.")