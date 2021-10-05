"""
Author:  Russell Gerhard
Purpose: Provide an abstract collection superclass for inheritance
         by any implementation of a specific abstract collection.

Exports:
    AbstractCollection: Abstract class providing some common implementations
                        of methods for collection types.
"""

class AbstractCollection(object):
    """
    Implement methods common to all implementations of the collections ADTs.
    """
    
    # Constructor
    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        self.length = 0
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
            raise TypeError("cannot concatenate bag with different type")
        # Instantiate new object of type self
        out = type(self)(self)
        for item in other:
            out.add(item)
        return out

    def copy(self):
        """Return a copy of self."""
        return type(self)(self)

    def count(self, item):
        """Return number of instances of item in self."""
        count = 0
        for obj in self:
            if obj == item:
                count += 1
        return count

    def __eq__(self, other):
        """
        Determine if self is equal to other.
        Return True if self and other are of same type, have the same length,
        and contain the same items in the same ordering, else return False.
        """
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        elif len(self) != len(other):
            return False
        else:
            other_iter = iter(other)
            for item in self:
                if item != next(other_iter):
                    return False
            return True
        
    def is_empty(self):
        """Return True if there are no items in self, else return False."""
        return (len(self) == 0)

    def __len__(self):
        """Return the number of items in self."""
        return self.length

    def __repr__(self):
        """Return the unique string representation of self."""
        out = f"{type(self).__name__}(" + ", ".join(map(str, self)) + ")"
        return out

    def __str__(self):
        """Return the string representation of self."""
        return '[' + ", ".join(map(str, self)) + ']'
