"""
Author:  Russell Gerhard
Purpose: Implement methods common to all set implementations in a base class.

Exports:
    AbstractSet: Base class that serves as a repository for
                 implementation-agnostic methods of the set ADT.
"""

class AbstractSet:
    """Store code for implementation-agnostic set methods."""

    # Accessors
    def __and__(self, other):
        """
        Return the intersection of self and other.
        Precondition: other must be of same type as self.
        Raises: TypeError
        """
        if type(self) != type(other):
            msg = "Cannot take intersection of objects with different types."
            raise TypeError(msg)
        else:
            intersection = type(self)()
            for item in self:
                if item in other:
                    intersection.add(item)
            return intersection

    def __eq__(self, other):
        """Return True if self is equal to other, else return False."""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        elif len(self) != len(other):
            return False
        else:
            for item in self:
                if not item in other:
                    return False
            return True
        
    def is_subset(self, other):
        """
        Return True if self is a subset of other.
        Precondition: other must be of same type as self.
        Raises: TypeError
        """
        if type(self) != type(other):
            msg = "Cannot check if self is subset of object with different type."
            raise TypeError(msg)
        else:
            for item in self:
                if not item in other:
                    return False
            return True

    def __or__(self, other):
        """
        Return the union of self and other.
        Precondition: other must be of same type as self.
        Raises: TypeError
        """
        if type(self) != type(other):
            msg = "Cannot take union of objects with different types."
            raise TypeError(msg)
        else:
            return self + other

    def __sub__(self, other):
        """
        Return set difference self - other. Items in self that are not in other.
        Precondition: other must be of same type as self.
        Raises: TypeError
        """
        if type(self) != type(other):
            msg = "Cannot take union of objects with different types."
            raise TypeError(msg)
        else:
            difference = type(self)()
            for item in self:
                if not item in other:
                    difference.add(item)
            return difference
