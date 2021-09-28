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

    def __iter__(self):
        """Support iteration over all items in self."""
        return None

    def __len__(self):
        """Return the number of items in self."""
        return 0

    def __repr__(self):
        """Return unique representation of self."""
        return ''

    def __str__(self):
        """Return the string representation of self."""
        return ''

    # Mutator Methods
    def clear(self):
        """Remove all items from self."""
        pass

    # Only difference from bag
    def add(self, item):
        """Add item to self if not already in self."""
        pass

    def remove(self, item):
        """
        Remove item from self.
        Precondition: Item is in self.
        Raises: ValueError if item is not in self.
        Postcondition: Item is not in self.
        """
        pass






        