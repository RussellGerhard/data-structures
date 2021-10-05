"""
Author:  Russell Gerhard
Purpose: Document functionality of methods for any class implementing the
         binary search tree (BST) ADT.
"""

class BSTInterface:
    """Specify interface for classes implementing a BST."""

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
        Create a copy of self and add each item in other to this copy of self.
        Precondition: other is of same type as self.
        Raises: TypeError
        """
        return None

    def __contains__(self, item):
        """Return True if item is in self, else return False."""
        return True

    def copy(self):
        """Return a copy of self."""
        return None

    def count(self, item):
        """Return number of instances of item in self."""
        return 0

    def __eq__(self, other):
        """
        Return True if other is of same type and has the same items in
        corresponding positions, else return False.
        """
        return True

    def find(self, item):
        """Return item if in tree, else return None."""
        return None

    def is_empty(self):
        """Return True if there are no items in self, else return False."""
        return True

    def __iter__(self):
        """Support iteration via a preorder traversal of self."""
        return None

    def __len__(self):
        """Return the number of items in self."""
        return 0

    def __repr__(self):
        """Return the unique string representation of self."""
        return ''

    def __str__(self):
        """Return string representation of self."""
        return ''

    # Iterator Accessors
    def inorder(self):
        """Return an iterator that performed an inorder traversal of self."""
        return None
    
    def levelorder(self):
        """Return an iterator that performed an levelorder traversal of self."""
        return None
    
    def postorder(self):
        """Return an iterator that performed an postorder traversal of self."""
        return None

    def preorder(self):
        """Return an iterator that performed an preorder traversal of self."""
        return None
    
    # Mutators
    def add(self, item):
        """Add item to self, increment length."""
        pass
    
    def clear(self):
        """Remove all items from self, set length to 0."""
        pass

    def remove(self, item):
        """
        Remove item from self, decrement length.
        Precondition: Item must be in self.
        Raises: LookupError
        """
        pass

    
    
