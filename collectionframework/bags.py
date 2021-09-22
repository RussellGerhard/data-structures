from abstractbag import AbstractBag
from array import Array
from linkedlist import LinkedList

"""
Author:  Russell Gerhard
Purpose: Implement bag ADT using an array or linked list, implement a sorted bag
         using an array and inheriting from the array-implemented bag.

Exports:
    ArrayBag: Bag ADT implementation using an array.
    ArraySortedBag: Sorted bag ADT implementation using an array.
    LinkedBag: Bag ADT implementation using a linked list.
"""

class ArrayBag(AbstractBag):
    """Implement bag ADT using an array."""
    default_capacity = 10

    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        self.items = Array(ArrayBag.default_capacity)
        self.position = -1
        AbstractBag.__init__(self, source_collection)
        
    # Accessors
    def __contains__(self, item):
        """
        Return True if item in self, set self.position to index.
        Else return False.
        """
        for obj in self:
            self.position += 1
            if item == obj:
                return True
        self.position = -1
        return False
    
    def __iter__(self):
        """Support iteration over self."""        
        i = 0
        while i < len(self):
            yield self.items[i]
            i += 1

    # Mutators
    def clear(self):
        """Empty self, reset length to 0 and position tracker to -1."""
        self.length = 0
        self.position = -1
        self.items = Array(ArrayBag.default_capacity)

    def add(self, item):
        """Add item to self, increase capacity of underlying array if necessary."""
        self.items.insert(len(self), item)
        self.length += 1

    def remove(self, item):
        """
        Remove item from self.
        Precondition: Item is in self.
        Raises: ValueError if item is not in self.
        Postcondition: Item is not in self.
        """
        # Reset position and check precondition
        self.position = -1
        if item not in self:
            raise ValueError("ArrayBag.remove(x): x not in ArrayBag")
        
        # Remove target item
        self.items.pop(self.position)

        # Decrement length
        self.length -= 1


class ArraySortedBag(ArrayBag):
    
    # Accessors
    def __contains__(self, item):
        """
        Determine if self contains item.
        Return True if so, else return False.
        """

        left = 0
        right = len(self) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if item < self.items[mid]:
                right = mid - 1
            elif item > self.items[mid]:
                left = mid + 1
            else:
                self.position = mid
                return True
        
        return False

    def __eq__(self, other):
        """
        Determine if self is equal to other.
        Return True if self and other of same type and contain same items.
        Return False else.
        """
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        elif len(self) != len(other):
            return False
        else:
            for (item1, item2) in zip(self, other):
                if item1 != item2:
                    return False
        return True

    # Mutators  
    def add(self, item):
        """
        Add item to self, increase length, increase capacity as needed.
        Item must be comparable, else raises ValueError.
        Precondition: self is sorted.
        Postcondition: self is sorted.
        """
        
        # Binary search for index position
        left = 0
        right = len(self) - 1
        mid = 0
        
        while left <= right:
            mid = (left + right) // 2
            if item > self.items[mid]:
                left = mid + 1
            elif item < self.items[mid]:
                right = mid - 1
            else:
                break

        # Insert in correct position
        if self.is_empty():
            self.items.insert(0, item)
        elif item > self.items[mid]:
            self.items.insert(mid + 1, item)
        else:
            self.items.insert(mid, item)
            
        self.length += 1


class LinkedBag(AbstractBag):
    """Implement bag ADT using a linked list."""

    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        self.items = LinkedList()
        self.position = -1
        AbstractBag.__init__(self, source_collection)

    # Accessors
    def __contains__(self, item):
        """
        Return true and set self.position to item index if item in self.
        Else return False.
        """
        self.position = -1
        for obj in self:
            self.position += 1
            if item == obj:
                return True
        return False
    
    def __iter__(self):
        """Support iteration over the object to visit each item."""
        probe = self.items.head
        while probe != None:
            yield probe.data
            probe = probe.next

    # Mutators
    def clear(self):
        """Empty self, reset length to 0 and position tracker to -1."""
        self.length = 0
        self.items = LinkedList()

    def add(self, item):
        """Add item to self."""
        self.items.insert(0, item)
        self.length += 1

    def remove(self, item):
        """
        Remove item from self.
        Precondition: Item is in self.
        Raises: ValueError if item is not in self.
        Postcondition: Item is not in self.
        """
        # Reset position and check precondition
        self.position = -1
        if item not in self:
            raise ValueError("LinkedBag.remove(x): x not in LinkedBag")
            
         # Remove target item
        self.items.pop(self.position)

        # Decrement length
        self.length -= 1
