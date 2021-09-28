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

    # Mutators
    def add(self, item):
        """Same as push, used to satisfy interface requirements."""
        self.push(item)
        
