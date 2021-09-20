from abstractcollection import AbstractCollection

"""
Author: Russell Gerhard
Provide an abstract bag superclass for inheritance by bag implementations.
"""

class AbstractBag(AbstractCollection):
    """
    Implement methods common to all implementations of the bag ADT.
    """
    default_capacity = 10

    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        AbstractCollection.__init__(self)
        self.mod_count = 0

        if source_collection:
            for item in source_collection:
                self.add(item)

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

    def __repr__(self):
        """Return the representation of self."""
        return '"' + str(self) + '"'
    
    def __str__(self):
        """Return the string representation of self."""
        return '{' + ", ".join(map(str, self)) + '}'
            
if __name__ == "__main__":
    pass
