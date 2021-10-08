"""
Author:  Russell Gerhard
Purpose: Provide a class to implement the heap ADT.

Exports:
    ArrayHeap: Implement the heap ADT with an array.
"""

from abstractclasses.abstractcollection import AbstractCollection
from dynamicarray import Array
from math import floor, log

class ArrayHeap(AbstractCollection):
    """Implement the heap ADT according to the heap interface using an array."""

    # Constructor
    def __init__(self, source_collection = None):
        """Initialize self, optionally add items from source_collection."""
        self.items = Array()
        AbstractCollection.__init__(self, source_collection)

    # Accessors
    def __eq__(self, other):
        """
        Return True if other is of same type and has the same items,
        else return False.
        """
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        elif len(self) != len(other):
            return False
        else:
            for item in self:
                if self.count(item) != other.count(item):
                    return False
            return True
        
    def __iter__(self):
        """
        Support iteration by visiting every item in the heap.
        No particular order is guaranteed.
        """
        for item in self.items:
            yield item
    
    def peek(self):
        """
        Return topmost item in self.
        Precondition: self is not empty.
        Raises: LookupError
        """
        # Check precondition
        if self.is_empty():
            raise LookupError("Cannot peek at empty heap.")

        return self.items[0]

    def __str__(self):
        """Return string representation of self."""
        # Empty
        if self.is_empty():
            return ''
        
        # Calculate height to determine width of tree display
        # This height formula only works for complete binary trees!
        height = 0 if len(self) == 0 else floor(log(len(self), 2) + 1)
        width = 2**(height + 1)

        # Set out string and initialize helpful traversal variables
        out = ''

        # Iterate through self.items, nodes are stored in level order
        width_break = 1
        for node_count, node in enumerate(self):
            # Check if this node will be on new level
            if log(node_count + 1, 2) % 1 == 0 and node_count != 0:
                out += "\n\n"
                width_break *= 2
            out += f"{node:^{width // width_break}}"

        return out

    # Mutators
    def add(self, item):
        """
        Insert item in proper place in self, increment length.
        Precondition: Item must be comparable and comparable to elements in
                      self.
        Raises: TypeError
        """
        # Check preconditions
        try:
            item < item
        except TypeError:
            raise TypeError("heap.add(item): item must be comparable.")

        if not self.is_empty():
            try:
                item < self.peek()
            except TypeError:
                msg = "heap.add(item): item must be comparable to other items"
                msg += " currently in heap."
                raise TypeError(msg)

        # Grow underlying array if necessary and add item to bottom
        self.items.grow()
        index = len(self)
        self.items[index] = item

        # Swap parent and item as long as parent is larger than item
        while index > 0:
            parent_index = (index - 1) // 2
            if self.items[parent_index] <= item:
                break
            else:
                self.items[index] = self.items[parent_index]
                self.items[parent_index] = item
            index = parent_index

        self.length += 1

    def clear(self):
        """Remove all items in self and reset length to 0."""
        self.items = Array()
        self.length = 0

    def pop(self):
        """
        Remove and return topmost item in self, decrement length.
        Precondition: self is not empty.
        Raises: LookupError
        """
        # Check precondition
        if self.is_empty():
            raise LookupError("Cannot pop from empty heap.")

        # Save return and move bottom element to top
        return_val = self.items[0]
        self.items[0] = self.items[len(self) - 1]
        parent_index = 0
        left_index = (parent_index * 2) + 1
        right_index = (parent_index * 2) + 2

        # Decrement length, if heap is now empty, return
        self.length -= 1
        self.items.logical_size -= 1
        if self.is_empty():
            return return_val

        # Move down heap, swapping large value at top with smallest child
        # If children larger than value at any point, stop!
        while True:
            no_r = False
            if left_index >= len(self):
                break
            if right_index >= len(self):
                no_r = True

            if self.items[left_index] >= self.items[parent_index] and \
               (no_r or self.items[right_index] >= self.items[parent_index]):
                break
            
            temp = self.items[parent_index]
            # no_r will trigger conditional before IndexError
            if no_r or (self.items[left_index] <= self.items[right_index]):
                self.items[parent_index] = self.items[left_index]
                self.items[left_index] = temp
                parent_index = left_index
            else:
                self.items[parent_index] = self.items[right_index]
                self.items[right_index] = temp
                parent_index = right_index
                
            # Recalculate indices
            left_index = (2 * parent_index) + 1
            right_index = (2 * parent_index) + 2

        # Shrink underlying array if necessary
        self.items.shrink()
        return return_val
        
