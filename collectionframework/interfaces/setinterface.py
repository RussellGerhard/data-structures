"""
Author:  Russell Gerhard
Purpose: Lay blueprint (interface) for any class implementing set ADT.
"""

class SetInterface:
    """Specify interface for classes implementing set ADT."""

    # Constructor
    def __init__(self, source_collection = None):
        """Set initial state of self, including optional contents of source."""
        pass

    # Accessor Methods
    def __add__(self, other):
        """
        Return a new set containing the contents of self and other.
        Precondition: other must be of type set.
        Raises: TypeError if other is not a set.
        """
        return None

    def __and__(self, other):
        """
        Return the intersection of self and other.
        Precondition: other must be of same type as self.
        Raises: TypeError
        """
        return None

    def clone(self):
        """Return copy of self."""
        return None

    def count(self, item):
        """Returns the number of instances of item in self."""
        return 0

    def __eq__(self, other):
        """Return True if self is equal to other, else return False."""
        return True
    
    def is_empty(self):
        """Return True if len(self) == 0, else return False."""
        return True

    def is_subset(self, other):
        """
        Return True if self is a subset of other.
        Precondition: other must be of same type as self.
        Raises: TypeError
        """
        return True

    def __iter__(self):
        """Support iteration over all items in self."""
        return None

    def __len__(self):
        """Return the number of items in self."""
        return 0

    def __or__(self, other):
        """
        Return the union of self and other.
        Precondition: other must be of same type as self.
        Raises: TypeError
        """
        return None

    def __repr__(self):
        """Return unique representation of self."""
        return ''

    def __str__(self):
        """Return the string representation of self."""
        return ''

    def __sub__(self, other):
        """
        Return set difference self - other. Items in self that are not in other.
        Precondition: other must be of same type as self.
        Raises: TypeError
        """
        return None

    # Mutator Methods
    # Only difference from bag
    def add(self, item):
        """If item not in self, add item and increment length."""
        pass
    
    def clear(self):
        """Remove all items from self, set length to 0."""
        pass

    def remove(self, item):
        """
        Remove item from self and decrement length.
        Precondition: Item is in self.
        Raises: ValueError if item is not in self.
        Postcondition: Item is not in self.
        """
        pass






        
