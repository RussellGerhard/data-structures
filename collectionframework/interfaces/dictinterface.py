"""
Author:  Russell Gerhard
Purpose: Document methods for any class implementing the dictionary ADT.
"""

class DictInterface:
    """Specify interface for classes implementing a dictionary."""

    # Constructor
    def __init__(self, keys = None, values = None):
        """
        Instantiate self and initialize with keys and values from constructor
        arguments, if present.
        Precondition: keys and values must be iterables with same length
        Raises: ValueErrors
        """
        pass

    # Accessors
    def __add__(self, other):
        """
        Create a copy of self, add all keys from other to this copy. If a key
        in other is same as a key from self, overwrite the value from self with
        the value from other.
        Precondition: other must be of same type as self.
        Raises: TypeError
        """
        return None

    def __contains__(self, key):
        """Return True if key is in self, else return False."""
        return True

    def copy(self):
        """Return a copy of self."""
        return None

    def count(self, item):
        """Return number of instances of item in all values in self."""
        return 0
    
    def entries(self):
        """Return an iterator on the entries in self."""
        return None

    def __eq__(self, other):
        """
        Return True if self and other have same keys with same corresponding values.
        """
        return True
    
    def get(self, key, default_value = None):
        """
        Return value associated with key if it is in self, else return the
        value provided in default_value parameter.
        """
        return None
    
    def __getitem__(self, key):
        """
        Return the value associated with key.
        Precondition: key must be in self.
        Raises: KeyError
        """
        return None

    def __iter__(self):
        """Return an iterator on the keys in self."""
        return None

    def keys(self):
        """Return an iterator on the keys in self."""
        return None

    def __repr__(self):
        """Return the unique string representation of self."""
        return ''

    def __str__(self):
        """Return a string representation of self."""
        return ''

    def values(self):
        """Return an iterator on the values in self."""
        return None        
    
    # Mutators
    def clear(self):
        """Remove every item in self and set length to 0."""
        pass
    
    def pop(self, key, default_value = None):
        """
        If key is in self, remove it and return the associated value, else
        return default_value.
        """
        return None
    
    def __setitem__(self, key, value):
        """
        If key is in self, replace its value with the argument passed, else
        create a new key in self and associated the value argument with it.
        """
        pass
    
