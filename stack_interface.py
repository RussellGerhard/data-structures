"""
Author: Russell Gerhard
Document the interface for the stack ADT.
"""

class StackInterface:
    def __init__(self, source_collection = None):
        """
        Initialize self, optionally pushing each element
        of source_collection onto the stack.
        """
        pass

    # Accessors
    def __add__(self, other):
        """
        Push each item in other onto a copy of self, return this concatentation.
        Precondition: other must be of type self.
        Raises: TypeError
        """
        return None
        
    def __contains__(self, item):
        """Return True if item in self, else return False."""
        return True

    def __eq__(self, other):
        """
        Return True if self and other of same type, same length, and contain
        the same items in the same order.
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
        Return item at top of self.
        Precondition: self is not empty.
        Raises: KeyError
        """
        return 0

    def __repr__(self):
        """Return the unique string representation of self."""
        return ''

    def __str__(self):
        """Return string representation of self."""
        return ''

    # Mutators
    def clear(self):
        """Remove every item from self, set length to 0."""
        pass

    def pop(self):
        """
        Remove and return item at top of self.
        Precondition: self is not empty.
        Rasies: KeyError
        """
        pass

    def push(self, item):
        """Add item to the top of s."""
        pass
        
