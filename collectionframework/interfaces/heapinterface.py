"""
Author:  Russell Gerhard
Purpose: Document functionality of methods for any class implementing the
         heap ADT.
"""

class HeapInterface:
    """Specify interface for classes implementing a heap."""

    # Constructor
    def __init__(self, source_collection = None):
        """
        Instantiate and initialize self, optionally adding each item in
        source_collection to self.
        """
        pass

    # Accessors
    def __add__(self, other):
        """
        Create a copy of self, then add each item in other to this copy of self.
        Return this copy.
        Precondition: other is of same type as self.
        Raises: TypeError
        """
        return None

    def __contains__(self, item):
        """Return True if item in self, else return False."""
        return True

    def copy(self):
        """Return a copy of self."""
        return None

    def count(self, item):
        """Return number of instances of item in self."""
        return 0

    def __eq__(self, other):
        """
        Return True if other is of same type and has the same items,
        else return False.
        """
        return True

    def is_empty(self):
        """Return True if there are no items in self, else return False."""
        return True

    def __iter__(self):
        """
        Support iteration by visiting every item in the heap.
        No particular order is guaranteed.
        """
        return None

    def __len__(self):
        """Return the number of items in self."""
        return 0
    
    def peek(self):
        """
        Return topmost item in self.
        Precondition: self is not empty.
        Raises: LookupError
        """
        return None

    def __repr__(self):
        """Return the unique string representation of self."""
        return ''

    def __str__(self):
        """Return string representation of self."""
        return ''

    # Mutators
    def add(self, item):
        """
        Insert item in proper place in self, increment length.
        Precondition: Item must be comparable and comparable to elements in
                      self.
        Raises: TypeError
        """
        pass

    def clear(self):
        """Remove all items from self, set length to 0."""
        pass

    def pop(self):
        """
        Remove and return topmost item in self, decrement length.
        Precondition: self is not empty.
        Raises: LookupError
        """
        pass
    
        
    
        
