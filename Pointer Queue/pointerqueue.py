#!/usr/bin/env python

#-----Queue: Pointer Implementation - CT482

class CellType: # Node
    elem = None
    next = None

    def __init__(self):
        self.elem = None
        self.next = None

    def __str__(self):
        return str(self.elem)

class pointerqueue:
    rear = CellType()
    curr = CellType()
    front = CellType()

    def __init__(self):
        self.rear = CellType()
        self.curr = CellType()
        self.front = CellType()
        return

# -----FRONT(Q) is a function that returns the first element on queue Q. It can be written in terms of list operations as RETRIEVE(FIRST(Q),Q)
    def FRONT(self):
        return self.front.elem #Returns the first element of the front of the queue

# -----ENQUEUE(x, Q) inserts element x at the end of queue Q.
    def ENQUEUE(self, x):
        if self.EMPTY(): # If queue is empty simply make a new node and point the front&rear to it
            newNode = CellType()
            newNode.elem = x
            newNode.next = None
            self.rear = newNode
            self.front = newNode
        else:
            # Increment rear pointer to point next empty space.
            # Create a new node and then copy current rear to it
            oldRear = CellType()
            oldRear.elem = self.rear.elem
            oldRear.next = self.rear.next

            # Set new rear to x
            self.rear.elem = x
            self.rear.next = oldRear  # Points to the node ahead, oldRear
            if(self.front.next != None):  # If there is something ahead of the front node, make that the new front
                self.front = self.front.next


# -----DEQUEUE(Q) deletes the first element of Q
    def DEQUEUE(self):
        prev = None
        if not self.EMPTY():
            cur = self.rear
            while cur != None: # While the queue exists
                if cur.next == self.front: # If the front of queue is reached, set prev to previous of front of queue
                    prev = cur
                cur = cur.next

            if prev != None: # If prev exists
                prev.next = None # Make prev point to nothing (as if it is front of queue)
                self.front = prev #Make prev the new front
            else: #If prev doesn't exist
                self.front = None
                self.rear = None
        else: #If empty, return
            return

# -----EMPTY(Q) returns true if and only if Q is an empty queue
    def EMPTY(self):
        if (self.rear.elem == None) and (self.curr.elem == None) and (self.front.elem == None):
            return True
        else:
            return False

# -----MAKENULL(Q) makes queue Q an empty list
    def MAKENULL(self):
        # Assuming python takes care of memory management
        # Reset the front and rear of the list
        self.rear = CellType()
        self.curr = CellType()
        self.front = CellType()
        return

# -----PRINTQ(Q) prints out the queue
    def PRINTQ(self):
        curr = self.rear
        output = curr.__str__()
        curr = curr.next
        while curr != None:
            if curr.elem != None:
                output = (output + ", " + curr.__str__())
            curr = curr.next
        return output