"""
Author:  Russell Gerhard
Purpose: Provide singly linked list.

Exports:
    LinkedList: List implementation based on singly-linked nodes.
"""

from nodes import Node

class LinkedList:
    """Represent a singly-linked list."""
    def __init__(self, head = None):
        """Instantiate an empty linked list."""
        self.head = head
        self.length = 0

    # Accessors
    def __contains__(self, item):
        if self.index(item) == -1:
            return False
        else:
            return True
            
    def copy(self):
        """Return a copy of self."""        
        # Traverse self and add each Node to duplicate
        probe = self.head
        duplicate = LinkedList(probe)
        while probe != None:
            duplicate.next = probe.next
            probe = probe.next
        return duplicate

    def count(self, item):
        """Count number of occurrences of item in self."""
        count = 0
        probe = self.head
        while probe != None:
            if probe.data == item:
                count += 1
            probe = probe.next
        return count
    
    def __getitem__(self, index):
        """
        Return item at index in self.
        Precondition: index in range(0, len(self)).
        Raises: IndexError
        """
        # Check precondition
        if index < 0:
            raise IndexError("LinkedList index cannot be negative.")
        
        # Traverse self to find index
        probe = self.head
        while probe != None and index != 0:
            probe = probe.next
            index -= 1
        if probe != None:
            return probe
        else:
            raise IndexError("LinkedList index out of range.")

    def index(self, item):
        """Return first index of value in self, else return -1."""
        index = 0
        probe = self.head
        while probe != None and probe.data != item:
            probe = probe.next
        if probe == None:
            return -1
        else:
            return probe.data

    def __len__(self):
        """Return length of self."""
        return self.length
        
    def __repr__(self):
        """Return the unique string representation of self."""
        out = ''
        # Traverse self to append all data
        probe = self.head
        while probe != None:
            out += f"{probe.data}, "
            probe = probe.next
        out = out[:-2]
        out = "'[" + out + "]'"
        return out
            
    def __str__(self):
        """Return string representation of self."""
        out = ''
        # Traverse self to append all data
        probe = self.head
        while probe != None:
            out += f"{probe.data}, "
            probe = probe.next
        out = out[:-2]
        out = '[' + out + ']'
        return out

    # Mutators
    def append(self, item):
        """Place item at end of self."""
        if self.head == None:
            self.head = Node(item, None)
        else:
            probe = self.head
            while probe.next != None:
                probe = probe.next
            probe.next = Node(item, None)
        self.length += 1

    def clear(self):
        """Clear self."""
        self.head = None
        self.length = 0

    def extend(self, iterable):
        """Extend self by appending items in iterable."""
        if self.head == None:
            self.head = Node(iterable[0], None)
            self.length += 1
            
            probe = self.head
            for item in iterable[1:]:
                probe.next = Node(item, None)
                self.length += 1
                probe = probe.next
        else:
            probe = self.head
            while probe.next != None:
                probe = probe.next

            for item in iterable:
                probe.next = Node(item, None)
                self.length += 1
                probe = probe.next

    def insert(self, index, item):
        """Insert item in self before index."""
        # Insert at head or self is empty
        if index <= 0 or self.head == None:
            self.head = Node(item, self.head)
            self.length += 1
        # Insert somewhere in rest of self
        else:
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            probe.next = Node(item, probe.next)
            self.length += 1

    def pop(self, index = 0):
        """
        Remove and return item at index.
        Precondition: self is not empty, index in range(0, len(self)).
        Raises: IndexError
        Postcondition: item at index is not in self.
        """
        # Check precondition
        if self.head == None:
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
                while index > 1 and probe.next.next != None:
                    probe = probe.next
                    index -= 1
                out = probe.next.data
                probe.next = probe.next.next
                self.length -= 1
                return out
            
    def remove(self, item):
        """
        Remove first occurence of item in self.
        Precondition: item must be in self.
        Raises: KeyError
        """
        probe = self.head
        if probe == None:
            raise KeyError("LinkedList.remove(x): x not in list")
        else:
             # Remove from beginning
            if probe.data == item:
                self.head = probe.next
                self.length -= 1
            # Remove from rest of self
            else:
                while probe.next != None and probe.next.data != item:
                    probe = probe.next
                if probe.next == None:
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
            # Traverse self with three pointers: island, probe1, and probe2
            while probe2.next != None:
                island = probe1
                probe1 = probe2
                probe2 = probe2.next
                probe1.next = island
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
        while probe != None and index != 0:
            probe = probe.next
            index -= 1
        if probe != None:
            probe.data = value
        else:
            raise IndexError("LinkedList index out of range.")

    def sort(self, reverse = False):
        """Use mergesort to sort contents of self."""
        copy_buffer = LinkedList()
        for _ in range(self.length):
            copy_buffer.prepend(None)
        self.sort_helper(copy_buffer, 0, self.length - 1)

        # List actually finishes in descending order
        # We have to reverse it to get a normal, ascending sort
        if not reverse:
            self.reverse()
        
    def sort_helper(self, copy_buffer, left, right):
        """Help with merge sort."""
        if left < right:
            mid = (left + right) // 2
            self.sort_helper(copy_buffer, left, mid)
            self.sort_helper(copy_buffer, mid + 1, right)
            self.merge(copy_buffer, left, mid, right)

    def merge(self, copy_buffer, left, mid, right):
        """Merge two sorted lists together."""
        index1 = left
        index2 = mid + 1
        copy_buffer = LinkedList()

        # Use copy_buffer to keep track of merged order
        for i in range(left, right + 1):
            if index1 > mid:
                copy_buffer.prepend(self[index2].data)
                index2 += 1
            elif index2 > right:
                copy_buffer.prepend(self[index1].data)
                index1 += 1
            # Prepending greatest instead of appending least
            elif self[index1].data > self[index2].data:
                copy_buffer.prepend(self[index1].data)
                index1 += 1
            else:
                copy_buffer.prepend(self[index2].data)
                index2 += 1

        # Keep reverse order in copy buffer so that next merge's prepends work
        copy_buffer.reverse()
                
        # Copy values over to self
        cb_ind = 0
        for i in range(left, right + 1):
            self[i] = copy_buffer[cb_ind].data
            cb_ind += 1
