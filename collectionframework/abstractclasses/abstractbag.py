"""
Author:  Russell Gerhard
Purpose: Provide an abstract bag superclass for inheritance by bag implementations.

Exports:
    AbstractBag: Abstract class providing some common implementations of
                 methods for bag types.
"""

from abstractclasses.abstractcollection import AbstractCollection

class AbstractBag(AbstractCollection):
    """ Implement methods common to all implementations of the bag ADT."""

    # Constructor
    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        AbstractCollection.__init__(self, source_collection)

    # Accessors
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
            for item in self:
                if self.count(item) != other.count(item):
                    return False
            return True
        
    def __str__(self):
        """Return string representation of self."""
        return '{' + ", ".join(map(str, self)) + '}'
