"""
Author:  Russell Gerhard
Purpose: Provide an abstract stack superclass for inheritance by stack
         implementations.

Exports:
    AbstractStack: Abstract class providing some common implementations of
                   methods for stack types.
"""

from abstractclasses.abstractcollection import AbstractCollection

class AbstractStack(AbstractCollection):
    """Implement methods common to all implementations of the stack ADT."""

    def __init__(self, source_collection = None):
        """Initialize self, optionally pushing items in source_collection."""
        AbstractCollection.__init__(self, source_collection)

    def __str__(self):
        """Return string representation of self."""
        return '[' + " | ".join(map(str, self)) + ']'

    # Mutators
    def add(self, item):
        """
        Same as push, used to satisfy interface requirements, increment length.
        """
        self.push(item)
        
