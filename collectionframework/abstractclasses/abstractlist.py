"""
Author:  Russell Gerhard
Purpose: Provide an abstract list superclass for inheritance from by list
         implementations.

Exports:
    AbstractList: Abstract class providing some implementation-agnostic methods
                  for list types.
"""

from abstractclasses.abstractcollection import AbstractCollection

class AbstractList(AbstractCollection):
    """Implement methods common to all implementations of the list ADT."""

    # Constructor
    def __init__(self, source_collection = None):
        AbstractCollection.__init__(self, source_collection)
    
    # Accessors
    def __getitem__(self, index):
        """
        Return item at index in self.
        Precondition: index in range(0, len(self)).
        Raises: IndexError
        """
        # Check precondition
        if index < 0:
            msg = f"{type(self).__name__} index cannot be negative."
            raise IndexError(msg)
        elif index >= len(self):
            msg = f"{type(self).__name__} index out of range."
            raise IndexError(msg)

        # Traverse self to find index
        for i, item in enumerate(self):
            if i == index:
                return item

    def index(self, item):
        """Return first index of value in self, else return -1."""
        for i, obj in enumerate(self):
            if obj == item:
                return i
        return -1

    # Mutators
    def add(self, item):
        """Append item to self."""
        self.append(item)

    def append(self, item):
        """Place item at end of self."""
        self.insert(len(self), item)
        
    def prepend(self, item):
        """Insert item at index 0."""
        self.insert(0, item)
    
