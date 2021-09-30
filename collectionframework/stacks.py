"""
Author:  Russell Gerhard
Purpose: Implement stack ADT using an array or doubly linked list.

Exports:
    ArrayStack: Stack ADT implementation using array.
    DoublyLinkedStack: Stack ADT implementation using a doubly linked list.*

*Doubly linked list is prefered to singly because the interface specifies that
 the iterator must move from bottom to top. Which would be O(n*2) in a singly
 linked list that keeps top at the head. A singly linked list can't keep top
 at the tail because there's no access so pushing, popping and peeking would be
 O(n). If iteration were to accur top to bottom, then singly link list would be
 OK.
"""

from abstractclasses.abstractstack import AbstractStack
from dynamicarray import Array
from lists import DoublyLinkedList

class ArrayStack(AbstractStack):
    """Implement stack ADT using an array."""
    default_capacity = 10

    def __init__(self, source_collection = None):
        """Initialize self, optionally pushing items from source_collection."""
        self.items = Array(ArrayStack.default_capacity)
        AbstractStack.__init__(self, source_collection)

    def __iter__(self): 
        """Support iteration over every item in self."""
        i = 0
        while i < len(self):
            yield self.items[i]
            i += 1

    def peek(self):
        """Return top item on self without popping it."""
        if self.is_empty():
            raise LookupError("Cannot peek at empty stack")
        
        return self.items[len(self) - 1]

    # Mutators
    def clear(self):
        """Remove all items from self, set length to 0."""
        self.items = Array(ArrayStack.default_capacity)
        self.length = 0

    def pop(self):
        """Remove top item from self and return it."""
        if self.is_empty():
            raise LookupError("Cannot pop from empty stack")
        
        # Top item is last item in array implementation
        out = self.items.pop(len(self) - 1)
        self.length -= 1
        return out
        

    def push(self, item):
        """Put item on top of stack."""
        self.items.insert(len(self), item)
        self.length += 1

        
class DoublyLinkedStack(AbstractStack):
    """Implement stack ADT using a doubly linked list."""

    def __init__(self, source_collection = None):
        """Initialize self, optionally pushing items from source_collection."""
        self.items = DoublyLinkedList()
        AbstractStack.__init__(self, source_collection)

    def __iter__(self): 
        """Support iteration over every item in self."""
        probe = self.items.head
        while probe != None:
            yield probe.data
            probe = probe.next

    def peek(self):
        """Return top item on self without popping it."""
        if self.is_empty():
            raise LookupError("Cannot peek at empty stack")
        
        return self.items.tail.data

    # Mutators
    def clear(self):
        """Remove all items from self, set length to 0."""
        self.items = DoublyLinkedList()
        self.length = 0

    def pop(self):
        """Remove top item from self and return it."""
        if self.is_empty():
            raise LookupError("Cannot pop from empty stack")

        out = self.items.pop(len(self) - 1)
        self.length -= 1
        return out

    def push(self, item):
        """Put item on top of stack."""
        self.items.insert(len(self), item)
        self.length += 1



        
