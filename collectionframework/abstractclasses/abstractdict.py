"""
Author:  Russell Gerhard
Purpose: Provide code for methods common to all classes implementing
         dictoinaries.

Exports:
    Entry: Container class for key-value pairs.

    AbstractDict: Implements methods common to all dictionary classes.
"""

from abstractclasses.abstractcollection import AbstractCollection

class Entry:
    """Contain key-value pairs."""

    # Constructor
    def __init__(self, key, value, probe_length = None):
        self.key = key
        self.value = value
        self.probe_length = probe_length

    # Accessors
    def __repr__(self):
        return "Entry(" + str(self) + ')'

    def __str__(self):
        return repr(self.key) + ": " + str(self.value)

class AbstractDict(AbstractCollection):

    # Constructor
    def __init__(self, keys = None, values = None):
        """
        Instantiate self and initialize with keys and values from constructor
        arguments, if present.
        Precondition: keys and values must be iterables with same length
        Raises: ValueError
        """
        AbstractCollection.__init__(self)
        if keys and values:
            if len(keys) != len(values):
                msg = f"Cannot initialize {len(keys)} keys with {len(values)} values."
                raise ValueError(msg)
            else:
                value_iter = iter(values)
                for key in keys:
                    value = next(value_iter)
                    self[key] = value

    # Accessors
    def __add__(self, other):
        """
        Create a copy of self, add all keys from other to this copy. If a key
        in other is same as a key from self, overwrite the value from self with
        the value from other.
        Precondition: other must be of same type as self.
        Raises: TypeError
        """
        if type(self) != type(other):
            msg = f"Cannot concatenate {type(self).__name__}"
            msg += " with object of different type."
            raise TypeError(msg)
        else:
            out = self.copy()
            for key in other:
                out[key] = other[key]
            return out

    def __contains__(self, key):
        """Return True if key is in self, else return False."""
        for self_key in self.keys():
            if key == self_key:
                return True
        return False

    def copy(self):
        """Return a copy of self."""
        return type(self)([key for key in self.keys()],
                          [val for val in self.values()])

    def count(self, value):
        """Return number of instances of item in all values in self."""
        out = 0
        for self_value in self.values():
            if value == self_value:
                out += 1
        return out
    
    def entries(self):
        """Return an iterator on the entries in self."""
        return map(lambda key: Entry(key, self[key]), self)

    def __eq__(self, other):
        """
        Return True if self and other have same keys with same corresponding values.
        """
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        elif len(self) != len(other):
            return False
        else:
            for key in self:
                if not key in other:
                    return False
            return True
    
    def get(self, key, default_value = None):
        """
        Return value associated with key if it is in self, else return the
        value provided in default_value parameter.
        """
        if key not in self:
            return default_value
        else:
            return self[key]

    def keys(self):
        """Return an iterator on the keys in self."""
        return iter(self)

    def __repr__(self):
        """Return the unique string representation of self."""
        out = f"{type(self).__name__}("
        out += ", ".join(map(str, self.entries()))
        out += ')'
        return out

    def __str__(self):
        """Return a string representation of self."""
        return '{' + ", ".join(map(str, self.entries())) + '}'

    def values(self):
        """Return an iterator on the values in self."""
        return map(lambda key: self[key], self)
    
