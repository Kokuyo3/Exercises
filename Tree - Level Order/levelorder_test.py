#!/usr/bin/env python

#Textbook Exercise 3.10: levelorder test - CT482

from levelorder import *

myTree = tree('h0_A') #Create root node

#Add child nodes, Height = 1
myTree.newChild(tree('h1_B'))
myTree.newChild(tree('h1_C'))

#Add child nodes, Height = 2
myTree.child[0].newChild(tree('h2_D'))
myTree.child[0].newChild(tree('h2_E'))

myTree.child[1].newChild(tree('h2_F'))
myTree.child[1].newChild(tree('h2_G'))
myTree.child[1].newChild(tree('h2_H'))

#Add child nodes, Height = 3
myTree.child[0].child[1].newChild(tree('h3_I'))
myTree.child[0].child[1].newChild(tree('h3_J'))
myTree.child[1].child[1].newChild(tree('h3_K'))
myTree.child[1].child[2].newChild(tree('h3_L'))
myTree.child[1].child[2].newChild(tree('h3_m'))

#Add child nodes, Height = 4
myTree.child[0].child[1].child[0].newChild(tree('h4_N'))
myTree.child[0].child[1].child[0].newChild(tree('h4_O'))
myTree.child[0].child[1].child[1].newChild(tree('h4_P'))

#Run levelorder(tree)
result = levelorder(myTree)

#Print and compare results
result = []
for n in result:
    result.append(n.cSpace)

print("Created Level Ordered Tree: " + str(result))
print "Expected Level Ordered Tree: ['h0_A', 'h1_B', 'h1_C', 'h2_D', 'h2_E', 'h2_F', 'h2_G', 'h2_H', 'h3_I', 'h3_J', 'h3_K', 'h3_L', 'h3_m', 'h4_N', 'h4_O', 'h4_P']"
