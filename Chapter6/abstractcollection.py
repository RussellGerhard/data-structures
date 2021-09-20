"""
Author: Russell Gerhard
Provide an abstract collection superclass for inheritance
by any implementation of a specific abstract collection.
"""

class AbstractCollection(object):
    """
    Implement methods common to all implementations of the collections ADTs.
    """
    default_capacity = 10

    def __init__(self):
        """Initialize self, optionally including items in source_collection."""
        self.size = 0

    # Accessors
    def __add__(self, other):
        """
        Return a bag that contains contents of self and other.
        Precondition: other must be of type bag.
        Raises: TypeError if other is not a bag.
        """
        # Check precondition
        if type(other) != type(self):
            raise TypeError("can only concatenate collections of different types")
        # Create new, abstract bag
        out = type(self)(self)
        for item in other:
            out.add(item)
        return out

    def clone(self):
        """Return copy of self."""
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
        Return True if self and other of same type and contain same items
        in the same order.
        Return False else.
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
                if item != next(other):
                    return False
            return True
        
    def is_empty(self):
        """Determine if self is empty, return True if it is, else False."""
        return (len(self) == 0)

    def __len__(self):
        """Return the number of items in self."""
        return self.size

    def __str__(self):
        """Return the string representation of self."""
        return '[' + ", ".join(map(str, self)) + ']'
            
if __name__ == "__main__":
    pass
