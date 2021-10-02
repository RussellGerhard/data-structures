"""
Author:  Russell Gerhard
Purpose: Document the interface of the queue ADT.
"""

class QueueInterface:
    """
    Specify the interface to which any class implementing the queue ADT must
    conform.
    """

    # Constructor
    def __init__(self, source_collection = None):
        """
        Initialize self, optionally adding each element of source_collection
        to self.
        """
        pass

    # Accessors
    def __add__(self, other):
        """
        Iterate through other, adding all items to a copy of self and return
        this copy.
        """
        return None

    def __contains__(self, item):
        """Return true if item in self, else return False."""
        return True

    def __eq__(self, other):
        """
        Return True if self and other of same type, same length, and contain
        the same items in the same order, else return False.
        """
        return True

    def is_empty(self):
        """Return True if len(self) == 0, else return False."""
        return True

    def __iter__(self):
        """Support iteration over every item in self."""
        return None

    def __len__(self):
        """Return number of items in self."""
        return 0

    def peek(self):
        """
        Return item at front of self.
        Precondition: self is not empty.
        Raises: LookupError
        """
        return 0

    def __repr__(self):
        """Return unique string representation of self."""
        return ''

    def __str__(self):
        """Return string representation of self."""
        return ''

    # Mutators
    def add(self, item):
        """Add item to rear of self, increment length."""
        pass
    
    def clear(self):
        """Remove every item from self, set length to 0."""
        pass

    def pop(self):
        """
        Remove and return item at front of self, decrement length.
        Precondition: self is not empty.
        Raises: LookupError
        """
        pass    
