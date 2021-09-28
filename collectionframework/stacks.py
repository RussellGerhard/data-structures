"""
Author:  Russell Gerhard
Purpose: Implement stack ADT using an array or linked list.

Exports:
    ArrayStack: Stack ADT implementation using array.
    LinkedStack: Stack ADT implementation using linked list.
"""

from abstractclasses.abstractstack import AbstractStack
from dynamicarray import Array
from linkedlist import LinkedList

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

    def __repr__(self):
        """Return the unique string representation of self."""
        return "ArrayStack(" + ", ".join(map(str, self)) + ')'

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
        self.length -= 1
        return self.items.pop(len(self) - 1)

    def push(self, item):
        """Put item on top of stack."""
        self.items.insert(len(self), item)
        self.length += 1


class LinkedStack(AbstractStack):
    """Implement stack ADT using a linked list."""

    def __init__(self, source_collection = None):
        """Initialize self, optionally pushing items from source_collection."""
        self.items = LinkedList()
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
        
        return self.items.head.data

    def __repr__(self):
        """Return the unique string representation of self."""
        return "LinkedStack(" + ", ".join(map(str, self)) + ')'

    # Mutators
    def clear(self):
        """Remove all items from self, set length to 0."""
        self.items = LinkedList()
        self.length = 0

    def pop(self):
        """Remove top item from self and return it."""
        if self.is_empty():
            raise LookupError("Cannot pop from empty stack")
        
        # Top item at head in linked list implementation, LinkedList.pop() defaults to head
        self.length -= 1
        return self.items.pop()

    def push(self, item):
        """Put item on top of stack."""
        self.items.insert(0, item)
        self.length += 1



        
