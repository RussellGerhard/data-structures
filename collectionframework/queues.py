"""
Author:  Russell Gerhard
Purpose: Implement Queue ADT using an array or doubly linked list.

Exports:
    ArrayQueue: Queue ADT implementation using array.
    DoublyLinkedQueue: Queue ADT implementation using a doubly linked list.
"""

from abstractclasses.abstractcollection import AbstractCollection
from dynamicarray import Array
from lists import DoublyLinkedList

class ArrayQueue(AbstractCollection):
    """Implement queue ADT using a circular array."""

    # Constructor
    def __init__(self, source_collection = None):
        """
        Initialize self, optionally adding each item in source_collection to
        self.
        """
        # I should implement a CircularArray class with front and rear
        # so that shrink actually works
        self.items = Array()
        self.front = 0
        self.rear = 0
        AbstractCollection.__init__(self, source_collection)

    # Accessors
    def __iter__(self):
        """Support iteration over every item in self from front to rear."""
        if self.front < self.rear:
            for i in range(self.front, self.rear + 1):
                yield self.items[i]
        elif self.rear < self.front:
            for i in range(self.front, self.items.capacity):
                yield self.items[i]
            for i in range(0, self.rear + 1):
                yield self.items[i]
        else:
            if not self.is_empty():
                yield self.items[self.front]
        
    def peek(self):
        """
        Return item at front of self.
        Precondition: self is not empty.
        Raises: LookupError
        """
        if self.is_empty():
            raise LookupError("Cannot peek at empty queue.")
        return self.items[self.front]

    # Mutators
    def add(self, item):
        """Add item to rear of self, increment length."""
        # Grow circular array if necessary
        if len(self) == self.items.capacity:

            # Copy items into array with double the capacity
            temp = Array(len(self)*2)

            for i, obj in enumerate(self):
                temp[i] = obj
            
            self.items.capacity = len(self)*2
            self.items = temp

            # Reset array pointers
            self.front = 0
            self.rear = len(self) - 1
             
        # Update rear
        if self.rear == self.items.capacity - 1:
            self.rear = 0
        elif self.is_empty():
            pass
        else:
            self.rear += 1

        # Add new item at rear and increment length
        self.items[self.rear] = item  
        self.length += 1

    def clear(self):
        """Remove every item from self, set length to 0."""
        self.items = Array()
        self.length = 0
        self.front = 0
        self.rear = 0

    def pop(self):
        """
        Remove and return item at front of self, decrement length.
        Precondition: self is not empty.
        Raises: LookupError
        """
        if self.is_empty():
            raise LookupError("Cannot pop from empty queue.")
        out = self.items[self.front]
        self.items[self.front] = None

        # Update front pointer
        if self.front == self.items.capacity:
            self.front = 0
        else:
            self.front +=1

        self.length -= 1
        return out

class DoublyLinkedQueue(AbstractCollection):
    """Implement queue ADT using a doubly linked list."""

    # Constructor
    def __init__(self, source_collection = None):
        """
        Initialize self, optionally adding each item in source_collection to
        self.
        """
        self.items = DoublyLinkedList()
        AbstractCollection.__init__(self, source_collection)

    # Accessors
    def __iter__(self):
        """Support iteration over every item in self from front to rear."""
        probe = self.items.head
        while probe != None:
            yield probe.data
            probe = probe.next
        
    def peek(self):
        """
        Return item at front of self.
        Precondition: self is not empty.
        Raises: LookupError
        """
        if self.is_empty():
            raise LookupError("Cannot peek at empty queue.")
        return self.items.head.data

    # Mutators
    def add(self, item):
        """Add item to rear of self, increment length."""
        self.items.append(item)
        self.length += 1
    
    def clear(self):
        """Remove every item from self, set length to 0."""
        self.items = DoublyLinkedList()
        self.length = 0

    def pop(self):
        """
        Remove and return item at front of self, decrement length.
        Precondition: self is not empty.
        Raises: LookupError
        """
        if self.is_empty():
            raise LookupError("Cannot pop from empty queue.")
        self.length -= 1
        return self.items.pop(0)
        
