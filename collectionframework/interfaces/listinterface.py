"""
Author:  Russell Gerhard
Purpose: Document functionality of methods for any class implementing list ADT.
"""

class ListInterface:
    """Specify interface for classes implementing a list."""

    # Constructor
    def __init__(self, source_collection = None):
        """
        Instantiate and initialize self, optionally appending each item in
        source_collection to self.
        """
        pass

    # Accessors
    def __add__(self, other):
        """
        Create copy of self and append each item in other to this copy,
        starting with the head of other. Return copy.
        Precondition: other is of same type as self.
        Raises: TypeError
        """
        return None

    def __contains__(self, item):
        """Return True if item in self, else False."""
        return True

    def copy(self):
        """Return a copy of self."""
        return None

    def count(self, item):
        """Count number of occurrences of item in self."""
        return 0

    def __eq__(self, item):
        """
        Determine if self is equal to other.
        Return True if self and other are of same type, have the same length,
        and contain the same items in the same ordering, else return False.
        """
        return True

    def __getitem__(self, index):
        """
        Return item at index in self.
        Precondition: index in range(0, len(self)).
        Raises: IndexError
        """
        return None

    def index(self, item):
        """Return first index of value in self, else return -1."""
        return 0

    def is_empty(self):
        """Return True if self empty, else False."""
        return True

    def __len__(self):
        """Return length of self."""
        return 0

    def __repr__(self):
        """Return the unique string representation of self."""
        return ''

    def __str__(self):
        """Return string representation of self."""
        return ''

    # Mutators
    def add(self, item):
        """Append an item to the end of self."""
        pass
    
    def append(self, item):
        """Place item at send of self."""
        pass

    def clear(self):
        """Clear self."""
        pass

    def extend(self, iterable):
        """Extend self by appending items in iterable."""
        pass

    def insert(self, index, item):
        """
        Insert item in self before index.
        If index is negative, insert before 0th item.
        If index is greater than len(self), append."""
        pass

    def prepend(self, item):
        """Insert item at index 0."""
        pass

    def pop(self, index = 0):
        """
        Remove and return item at index.
        Precondition: self is not empty, index in range(0, len(self)).
        Raises: IndexError
        Postcondition: item at index is not in self.
        """
        None

    def remove(self, item):
        """
        Remove first occurence of item in self.
        Precondition: item must be in self.
        Raises: KeyError
        """
        pass

    def reverse(self, item):
        """Reverse contents of self in place."""
        pass

    def __setitem__(self, index, value):
        """
        Set item at index to value.
        Precondition: index in range(0, len(self)).
        Raises: IndexError
        """
        pass

    def sort(self, reverse = False):
        """Use mergesort to sort contents of self."""
        pass
    
