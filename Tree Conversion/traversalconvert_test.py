from traversalconvert import *

print("Creating a list of elements...")
myList = ['1', '2', '3', '4', '5', '6', '7']
print("List: " + str(myList))

print("Converting pre to post and storing in variable, 'post'")
post = pre_post(myList)

print("Starting conversions:")
print("Pre to Post:" + str(post))

print("Post to Pre:" + str(post_pre(post)))

print("Pre to In: " + str(pre_in(myList)))
