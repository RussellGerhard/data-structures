from abstractcollection import AbstractCollection

"""
Author:  Russell Gerhard
Purpose: Provide an abstract bag superclass for inheritance by bag implementations.

Export:
    AbstractBag: Abstract class providing some commond implementations of
                 methods for bag types.
"""

class AbstractBag(AbstractCollection):
    """ Implement methods common to all implementations of the bag ADT."""
    default_capacity = 10

    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        AbstractCollection.__init__(self)
        if source_collection:
            for item in source_collection:
                self.add(item)

    # Accessors
    def __add__(self, other):
        """
        Return a collection that contains contents of self and other.
        Precondition: other must be same type as self
        Raises: TypeError
        """
        # Check precondition
        if type(other) != type(self):
            raise TypeError("cannot concatenate collections of different types")
        # Instantiate new object of type self
        out = type(self)(self)
        for item in other:
            out.add(item)
        return out
    
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
        """Return the string representation of self."""
        return '{' + ", ".join(map(str, self)) + '}'
