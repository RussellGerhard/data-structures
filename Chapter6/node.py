"""
Author: Russell Gerhard
Implement a simple node class.
"""

class Node:
    """Represent a singly-linked node."""
    def __init__(self, data, _next = None):
        """Instantiate a node."""
        self.data = data
        self.next = _next
        
    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return f"{self.data}"

class TwoWayNode(Node):
    """Represent a doubly-linked node."""
    def __init__(self, data, _next = None, prev = None):
        Node.__init__(self, data, _next)
        self.prev = prev

class LinkedList:
    """Represent a singly-linked list."""
    def __init__(self, head = None):
        """Instantiate an empty linked list."""
        self.head = head
        self.length = 0

    def __getitem__(self, index):
        probe = self.head
        while probe != None and index != 0:
            probe = probe.next
            index -= 1
        if probe != None:
            return probe
        else:
            raise IndexError("LinkedList index out of range")

    def __len__(self):
        """Return length of self."""
        return self.length
        
    def __repr__(self):
        """Get representation of the linked list."""
        out = ''
        probe = self.head
        while probe != None:
            out += f"{probe.data} "
            probe = probe.next
        return out

    def __setitem__(self, index, value):
        probe = self.head
        while probe != None and index != 0:
            probe = probe.next
            index -= 1
        if probe != None:
            probe.data = value
        else:
            raise IndexError("LinkedList index out of range")
            
    def __str__(self):
        """Get string representation of the linked list."""
        out = ''
        probe = self.head
        while probe != None:
            out += f"{probe.data} "
            probe = probe.next
        return out

    def append(self, item):
        """Append an item to the end of the list, O(n) time."""
        if self.head == None:
            self.head = Node(item, None)
        else:
            probe = self.head
            # Find tail node
            while probe.next != None:
                probe = probe.next
            probe.next = Node(item, None)

        self.length += 1

    def clear(self):
        """Clear list."""
        self.head = None
        self.length = 0

    def copy(self):
        """Make a copy of the list."""
        copy = LinkedList()
        probe = self.head
        while probe != None:
            copy.append(probe)
            probe = probe.next
        return copy

    def count(self, item):
        """Count number of instances of item in list."""
        count = 0
        probe = self.head
        while probe != None:
            if probe.data == item:
                count += 1
            probe = probe.next
        return count

    def disp(self):
        """Display like a stack."""
        probe = self.head
        while probe != None:
            print(probe)
            probe = probe.next

    def extend(self, iterable):
        """Extend list by appending items in iterable."""
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

    def index(self, item):
        """Return first index of value."""
        index = 0
        probe = self.head
        while probe != None and probe.data != item:
            probe = probe.next
        if probe == None:
            return -1
        else:
            return probe.data

    def insert(self, index, item):
        """Insert item before index."""
        if index <= 0 or self.head == None: # Insert at head or list empty
            self.head = Node(item, self.head)
            self.length += 1
        else: # Insert somewhere in rest
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            probe.next = Node(item, probe.next)
            self.length += 1

    def pop(self, index = 0):
        """Remove and return item at index."""
        if self.head == None:
            raise IndexError("pop from empty list")
        
        else:
            # Remove from head of list
            if index <= 0: 
                out = self.head.data
                self.head = self.head.next
                self.length -= 1
                return out
            
            # Trying to remove from second position or larger in singleton list
            elif index > 0 and self.head.next == None:
                raise IndexError("pop index out of range")

            # Remove from rest of list
            else:
                probe = self.head
                while index > 1 and probe.next.next != None:
                    probe = probe.next
                    index -= 1
                if index > 1:
                    raise IndexError("pop index out of range")
                out = probe.next.data
                probe.next = probe.next.next
                self.length -= 1
                return out

    def prepend(self, item):
        """Prepend an item to the list."""
        self.head = Node(item, self.head)
        self.length += 1

    def push(self, item):
        self.prepend(item)

    def remove(self, item):
        """Remove first occurence of value."""
        probe = self.head
        if probe == None: # List is empty
            raise ValueError("LinkedList.remove(x): x not in list")
        else:
            if probe.data == item: # Remove from beginning
                self.head = probe.next
                self.length -= 1
            else:
                while probe.next != None and probe.next.data != item:
                    probe = probe.next
                if probe.next == None:
                    raise ValueError("LinkedList.remove(x): x not in list")
                else:
                    probe.next = probe.next.next
                    self.length -= 1

    def reverse(self):
        """Reverse *IN PLACE*."""
        if self.length > 1:
            probe1 = self.head
            probe2 = self.head.next
            probe1.next = None
            while probe2.next != None:
                island = probe1
                probe1 = probe2
                probe2 = probe2.next
                probe1.next = island
            probe2.next = probe1
            self.head = probe2

    def sort(self, reverse = False):
        """(merge) sort the list IN PLACE in ascending order."""
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

        # This is the normal, assignment way, but assignment is an expensive
        # linear time operation for linked lists, so prepending and reversing
        # seems better to me.
        """
        # Use copy_buffer to keep track of merged order
        for i in range(left, right + 1):
            if index1 > mid:
                copy_buffer[i] = (self[index2].data)
                index2 += 1
            elif index2 > right:
                copy_buffer[i] = (self[index1].data)
                index1 += 1
            # Prepending greatest instead of appending least
            elif self[index1].data < self[index2].data:
                copy_buffer[i] = (self[index1].data)
                index1 += 1
            else:
                copy_buffer[i] = (self[index2].data)
                index2 += 1
                
        # Copy values over to self
        for i in range(left, right + 1):
            self[i] = copy_buffer[i].data
        """

def make_two_way(l: LinkedList) -> LinkedList:
    if l.head == None:
        l.tail = l.head
    else:
        probe = TwoWayNode(l.head.data, l.head.next, None)
        while probe.next != None:
            temp = probe
            probe = probe.next
            probe = TwoWayNode(probe, probe.next, temp)
        l.tail = probe
    
