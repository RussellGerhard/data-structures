"""
Author:  Russell Gerhard
Purpose: Provide classes implementing the list ADT using a dynamic array, singly
         linked list, and doubly linked list.

Exports:
    ArrayList: List implementation based on an array.

    LinkedList: List implementation based on singly-linked nodes.
    
    DoublyLinkedList: Linked list with tail pointer whose nodes have pointers
                      to previous nodes.
"""

from dynamicarray import Array
from nodes import Node, TwoWayNode
from abstractclasses.abstractlist import AbstractList

class ArrayList(AbstractList):
    """Represent a dymanic-array-based list."""
    def __init__(self, source_collection = None):
        """
        Instantiate and initialize self, optionally appending each item in
        source_collection to self.
        """
        self.items = Array()
        AbstractList.__init__(self, source_collection)

        
    # Accessors
    def __iter__(self):
        """Support iteration over all items in self."""
        for item in self.items:
            yield(item)

    # Mutators
    def clear(self):
        """Remove all items from self, set length to 0."""
        self.items = Array()
        self.length = 0

    def extend(self, iterable):
        """Extend self by appending each item in iterable."""
        for item in iterable:
            self.append(item)

    def insert(self, index, item):
        """Insert item in self before index, increment length."""
        if index < 0:
            self.items.insert(0, item)
        else:
            self.items.insert(index, item)
        self.length += 1

    def pop(self, index = 0):
        """
        Remove and return item at index, decrement length.
        Precondition: self is not empty, index in range(0, len(self)).
        Raises: IndexError
        """
        # Check precondition
        if self.is_empty():
            raise IndexError("pop from empty list")
        elif index < 0 or index >= len(self):
            raise IndexError("pop index out of range")
        else:
            return self.items.pop(index)

    def remove(self, item):
        """
        Remove first occurence of item in self, decrement length.
        Precondition: item must be in self.
        Raises: KeyError
        """
        if item not in self:
            raise KeyError("ArrayList.remove(x): x not in list")
        else:
            self.items.remove(item)
            self.length -= 1

    def reverse(self):
        """Reverse contents of self in place."""
        if self.length > 1:
            for i in range(self.length // 2):
                temp = self[i]
                self[i] = self[len(self) - (i + 1)]
                self[len(self) - (i + 1)] = temp

    def __setitem__(self, index, value):
        """
        Set item at index to value.
        Precondition: index in range(0, len(self)).
        Raises: IndexError
        """
        # Check precondition
        if index < 0:
            raise IndexError("ArrayList index cannot be negative.")
        elif index >= len(self):
            raise IndexError("ArrayList index out of range.")
        else:
            self.items[index] = value

    def sort(self, reverse = False):
        """Use quicksort to sort contents of self."""
        self.sort_helper(0, len(self) - 1)

        if reverse:
            self.reverse()

    def sort_helper(self, left, right):
        """Help sort method by hiding arguments needed for recursion."""
        if left < right:
            partition = self.partition(left, right)
            self.sort_helper(left, partition - 1)
            self.sort_helper(partition + 1, right)

    def partition(self, left, right):
        """
        Partition the part of self between left and right indices
        into parts whose elements are either less than or greater than
        the item at the middle of left and right, aka the pivot. Return the
        new position of the pivot, aka the border between the partitions.
        """
        # Establish pivot
        mid = (left + right) // 2
        pivot = self[mid]
        # Swap pivot with end
        temp = self[right]
        self[right] = pivot
        self[mid] = temp
        
        # Border of items less than pivot starts at left
        border = left
        for i in range(left, right):
            if self[i] < pivot:
                # Swap border item with small item, increase border
                temp = self[i]
                self[i] = self[border]
                self[border] = temp
                border += 1
            
        # Swap pivot and border item
        self[right] = self[border]
        self[border] = pivot

        return border


class LinkedList(AbstractList):
    """Represent a singly-linked list."""
    def __init__(self, source_collection = None):
        """
        Instantiate and initialize self, optionally appending each item in
        source_collection to self.
        """
        self.head = None
        AbstractList.__init__(self, source_collection)

    # Accessors
    def __iter__(self):
        """Support iteration over all items in self."""
        probe = self.head
        while probe is not None:
            yield(probe.data)
            probe = probe.next

    # Mutators
    def clear(self):
        """Remove all items from self, set length to 0."""
        self.head = None
        self.length = 0

    def extend(self, iterable):
        """Extend self by appending each item in iterable."""
        self.reverse()
        for item in iterable:
            self.prepend(item)
        self.reverse()

    def insert(self, index, item):
        """Insert item in self before index, increment length."""
        # Insert at head or self is empty
        if index <= 0 or self.is_empty():
            self.head = Node(item, self.head)
            self.length += 1
        # Insert elsewhere in self
        else:
            probe = self.head
            while index > 1 and probe.next is not None:
                probe = probe.next
                index -= 1
            probe.next = Node(item, probe.next)
            self.length += 1

    def pop(self, index = 0):
        """
        Remove and return item at index, decrement length.
        Precondition: self is not empty, index in range(0, len(self)).
        Raises: IndexError
        """
        # Check precondition
        if self.is_empty():
            raise IndexError("pop from empty list")
        elif index < 0 or index >= len(self):
            raise IndexError("pop index out of range")
        else:
            # Remove from head
            if index == 0: 
                out = self.head.data
                self.head = self.head.next
                self.length -= 1
                return out

            # Self must contain at least two items
            else:
                probe = self.head
                while index > 1 and probe.next.next is not None:
                    probe = probe.next
                    index -= 1
                out = probe.next.data
                probe.next = probe.next.next
                self.length -= 1
                return out
            
    def remove(self, item):
        """
        Remove first occurence of item in self, decrement lenght.
        Precondition: item must be in self.
        Raises: KeyError
        """
        probe = self.head
        if probe is None:
            raise KeyError("LinkedList.remove(x): x not in list")
        else:
             # Remove from beginning
            if probe.data == item:
                self.head = probe.next
                self.length -= 1
            # Remove from rest of self
            else:
                while probe.next is not None and probe.next.data != item:
                    probe = probe.next
                if probe.next is None:
                    raise KeyError("LinkedList.remove(x): x not in list")
                else:
                    probe.next = probe.next.next
                    self.length -= 1

    def reverse(self):
        """Reverse contents of self in place."""
        if self.length > 1:
            probe1 = self.head
            probe2 = self.head.next
            probe1.next = None
            # Traverse self with three pointers: last_node, probe1, and probe2
            while probe2.next is not None:
                last_node = probe1
                probe1 = probe2
                probe2 = probe2.next
                probe1.next = last_node
            probe2.next = probe1
            self.head = probe2
        
    def __setitem__(self, index, value):
        """
        Set item at index to value.
        Precondition: index in range(0, len(self)).
        Raises: IndexError
        """
        # Check precondition
        if index < 0:
            raise IndexError("LinkedList index cannot be negative.")
        # Traverse self to find index
        probe = self.head
        while probe is not None and index != 0:
            probe = probe.next
            index -= 1
        if probe is not None:
            probe.data = value
        else:
            raise IndexError("LinkedList index out of range.")

    def sort(self, reverse = False):
        """Use mergesort to sort contents of self."""
        self.sort_helper(0, self.length - 1)

        # List actually finishes in descending order
        # We have to reverse it to get a normal, ascending sort
        if not reverse:
            self.reverse()

    # Helper functions not designed to be called by user
    def sort_helper(self, left, right):
        """Help with merge sort."""
        if left < right:
            mid = (left + right) // 2
            self.sort_helper(left, mid)
            self.sort_helper(mid + 1, right)
            self.merge(left, mid, right)

    def merge(self, left, mid, right):
        """Merge two sorted lists together."""
        index1 = left
        index2 = mid + 1
        copy_buffer = LinkedList()

        # Use copy_buffer to keep track of merged order
        for i in range(left, right + 1):
            if index1 > mid:
                copy_buffer.prepend(self[index2])
                index2 += 1
            elif index2 > right:
                copy_buffer.prepend(self[index1])
                index1 += 1
            # Prepending larger item to copy_buffer
            elif self[index1] > self[index2]:
                copy_buffer.prepend(self[index1])
                index1 += 1
            else:
                copy_buffer.prepend(self[index2])
                index2 += 1

        # Keep reverse order in copy buffer so that next merge's prepends work
        copy_buffer.reverse()
                
        # Copy values over to self
        cb_ind = 0
        for i in range(left, right + 1):
            self[i] = copy_buffer[cb_ind]
            cb_ind += 1


class DoublyLinkedList(AbstractList):
    """Represent a doubly-linked list."""

    def __init__(self, source_collection = None):
        """
        Instantiate and initialize self, optionally appending each item in
        source_collection to self.
        """
        self.head = None
        self.tail = None
        AbstractList.__init__(self, source_collection)

    # Accessors
    def __iter__(self):
        """Support iteration over all items in self."""
        probe = self.head
        while probe is not None:
            yield(probe.data)
            probe = probe.next

    # Mutators
    def clear(self):
        """Remove all items from self, set length to 0."""
        self.head = None
        self.tail = None
        self.length = 0

    def extend(self, iterable):
        """Extend self by appending each item in iterable."""
        for item in iterable:
            self.append(item)

    def insert(self, index, item):
        """Insert item in self before index, increment length."""
        # Insert at head or self is empty
        if self.is_empty():
            self.head = TwoWayNode(item, None, None)
            self.tail = self.head
        elif index <= 0:
            self.head.prev = TwoWayNode(item, self.head, None)
            self.head = self.head.prev
        # Insert at end of self
        elif index >= len(self):
            self.tail.next = TwoWayNode(item, None, self.tail)
            self.tail = self.tail.next
        # Insert elsewhere in self
        else:
            probe = self.head
            while index > 1 and probe.next is not None:
                probe = probe.next
                index -= 1
            # Link current node to new node, give new node links
            probe.next = TwoWayNode(item, probe.next, probe)

            # If insert in middle, update prev of the node after inserted node
            if probe.next.next:
                probe.next.next.prev = probe.next
            else:
                self.tail = probe.next
        self.length += 1

    def pop(self, index = 0):
        """
        Remove and return item at index, decrement length.
        Precondition: self is not empty, index in range(0, len(self)).
        Raises: IndexError
        """
        # Check precondition
        if self.is_empty():
            raise IndexError("cannot pop from an empty list")
        elif index < 0 or index >= len(self):
            raise IndexError("pop index out of range")
        else:
            self.length -= 1
            
            # Remove from head
            if index == 0:
                out = self.head.data
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                return out
            # Remove from elsewhere
            else:
                probe = self.head
                while index > 1 and probe.next is not None:
                    probe = probe.next
                    index -= 1
                out = probe.next.data
                # Popped middle node, need to update a prev pointer
                if probe.next.next:
                    probe.next.next.prev = probe
                # Popped tail node, no prev pointer to update
                else:
                    self.tail = probe

                # Update probe.next to skip the popped node
                probe.next = probe.next.next
                return out

    def remove(self, item):
        """
        Remove first occurence of item in self, decrement length.
        Precondition: item must be in self.
        Raises: KeyError
        """
        if item not in self:
            raise KeyError("DoublyLinkedList.remove(x): x not in list")
        else:
            # Remove from beginning
            if self.head.data == item:
                self.head = self.head.next
                self.head.prev = None
                self.length -= 1
            # Remove from elsewhere
            else:
                probe = self.head
                while probe.next is not None:
                    if probe.next.data == item:
                        break
                    probe = probe.next

                # Removed from middle
                if probe.next.next:
                    probe.next.next.prev = probe
                # Removed tail
                else:
                    self.tail = probe

                # Update tail position and length
                probe.next = probe.next.next
                self.length -= 1
                    
    def reverse(self):
        """Reverse contents of self in place."""
        if self.length > 1:
            self.tail = self.head
            
            # Initialize traversal helpers
            probe1 = self.head
            probe2 = self.head.next

            # Probe2 stores our next value; we can safely set self.head.next to None
            probe1.next = None

            # Until probe2 reaches the tail, apply this process
            while probe2.next is not None:
                # Move everything forward
                last_node = probe1
                probe1 = probe2
                probe2 = probe2.next

                # Update pointers
                probe1.next = last_node
                probe1.prev = probe2
                last_node.prev = probe1
                
            # Probe2 has reached the old tail
            # So it's next is the previous probe, it's prev is None, and it is the head!
            probe2.next = probe1
            probe2.prev = None
            self.head = probe2

    def __setitem__(self, index, value):
        """
        Set item at index to value.
        Precondition: index in range(0, len(self)).
        Raises: IndexError
        """
        # Check precondition
        if index < 0:
            raise IndexError("LinkedList index cannot be negative")
        elif index >= len(self):
            raise IndexError("LinkedList index out of range.")

        # Traverse
        probe = self.head
        while probe is not None and index != 0:
            probe = probe.next
            index -= 1
        probe.data = value

    def sort(self, reverse = False):
        """Use mergesort to sort contents of self."""
        self.sort_helper(0, len(self) - 1)

        if reverse:
            self.reverse()

    def sort_helper(self, left, right):
        """Help with merge sort."""
        if left < right:
            mid = (left + right) // 2
            self.sort_helper(left, mid)
            self.sort_helper(mid + 1, right)
            self.merge(left, mid, right)

    def merge(self, left, mid, right):
        """Merge two sorted lists together."""
        index1 = left
        index2 = mid + 1
        copy_buffer = DoublyLinkedList()

        # Use copy_buffer to track merged order
        for i in range(left, right + 1):
            # Run out of element in one list
            if index1 > mid:
                copy_buffer.append(self[index2])
                index2 += 1
            elif index2 > right:
                copy_buffer.append(self[index1])
                index1 += 1
            # Appending smaller item to copy_buffer
            elif self[index1] < self[index2]:
                copy_buffer.append(self[index1])
                index1 += 1
            else:
                copy_buffer.append(self[index2])
                index2 += 1

        # Copy ordered values in buffer to self
        cb_ind = 0
        for i in range(left, right + 1):
            self[i] = copy_buffer[cb_ind]
            cb_ind += 1

