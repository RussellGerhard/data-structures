from bags import ArrayBag, ArraySortedBag, LinkedBag

"""
Author:  Russell Gerhard
Purpose: Implement set ADT using an array or linked list, implement a sorted set
         using an array and inheriting from a sorted, array-implemented bag.

Exports:
    ArraySet: Set ADT implementation using an array.
    
    ArraySortedSet: Sorted set ADT implementation using an array.
    
    LinkedSet: Set ADT implementation using a linked list.
"""
         
class ArraySet(ArrayBag):
    """Implement set ADT using an array, inheriting from ArrayBag."""
    def add(self, item):
        """
        If item not in self, add item to self.
        Increase length, increase capacity as needed.
        """
        if item not in self:
            self.items.insert(len(self), item)
            self.length += 1

class ArraySortedSet(ArraySortedBag):
    """Implement sorted set ADT using an array, inheriting from ArraySortedBag."""
    def add(self, item):
        """
        Add item to self if not already in self.
        Increase length if add performed, increase capacity as needed.
        Item must be comparable, else raises TypeError.
        Precondition: self is sorted.
        Postcondition: self is sorted.
        """
        # Duck typing!
        try:
            item < item
        except TypeError:
            raise TypeError("ArraySortedSet contains items that support comparison.")
            
        if item not in self:
            ArraySortedBag.add(self, item)

class LinkedSet(LinkedBag):
    """Implement set ADT using a linked list, inheriting from LinkedBag."""
    def add(self, item):
        """
        If item not in self, add item to self.
        Increase length if add performed.
        """
        if item not in self:
            self.items.insert(0, item)
            self.length += 1
