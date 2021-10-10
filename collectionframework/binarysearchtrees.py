"""
Author:  Russell Gerhard
Purpose: Provide a class to implement the binary search tree ADT.

Exports:
    LinkedBST: BST implemented with linked nodes.
"""

from abstractclasses.abstractcollection import AbstractCollection
from queues import DoublyLinkedQueue
from stacks import DoublyLinkedStack
from nodes import BSTNode

class LinkedBST(AbstractCollection):
    """Implement the BST ADT according to BST interface using linked nodes."""

    # Constructor
    def __init__(self, source_collection = None):
        """Initialize self, optionally add items from source_collection."""
        self.root = None
        AbstractCollection.__init__(self, source_collection)

    # Accessors
    def __contains__(self, item):
        """Return True if item in self, else return false."""
        if self.find(item) is None:
            return False
        else:
            return True
    
    def find(self, item):
        """Return item if in tree, else return None."""
        # Helper recursion fucntion
        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        return recurse(self.root)

    def get_height(self, node):
        """Determine height of subtree whose root is node."""
        if node == None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        elif node.left is None:
            return 1 + self.get_height(node.right)
        elif node.right is None:
            return 1 + self.get_height(node.left)
        else:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def is_balanced(self, node):
        """Return True if subtree whose root is node is balanced, else return False."""
        if node is None:
            return True
        else:
            if abs(self.get_height(node.left) - self.get_height(node.right)) > 1:
                return False
            else:
                return self.is_balanced(node.left) and self.is_balanced(node.right)
        
    def __iter__(self):
        """
        Support iteration with a generator that follows a preorder traversal of self.
        """
        node_stack = DoublyLinkedStack([self.root])
        while not node_stack.is_empty():
                node = node_stack.pop()
                if node:
                    yield(node.data)
                    node_stack.push(node.right)
                    node_stack.push(node.left)

    def __str__(self):
        """Return string representation of self."""
        # Empty
        if self.is_empty():
            return ''
        
        # Calculate height to determine width of tree display
        height = self.get_height(self.root)
        width = 2**(height + 1)

        # Set out string and initialize helpful traversal variables
        out = ''        

        # Append root value, centered in width
        out += f"{self.root.data:^{width}}\n\n"

        # Create queue for traversing nodes below root in level order
        node_queue = DoublyLinkedQueue([self.root])
        node_count = 1
        level = 1
        width_break = 2
        
        # Traverse nodes below root in level order
        while not node_queue.is_empty():
            # Get new node
            node = node_queue.pop()

            # Checked if this node is first on a new level
            if node_count == 2**level:
                out += '\n\n'
                width_break *= 2
                level += 1

            # Create next layer with whitespace-centered values

            # Check if parent is dummy node in queue
            if node is None:
                out += ' ' * (width // width_break) * 2
                # Add more dummy nodes to simulate full tree if node isn't a leaf
                if level != height:
                    node_queue.add(None)
                    node_queue.add(None)
            else:
                if node.left:
                    out += f"{node.left.data:^{width // width_break}}"
                    node_queue.add(node.left)
                else:
                    out += ' ' * (width // width_break)
                    # Add more dummy nodes to simulate full tree if node isn't a leaf
                    if level != height:
                        node_queue.add(None)
                if node.right:
                    out += f"{node.right.data:^{width // width_break}}"
                    node_queue.add(node.right)
                else:
                    out += ' ' * (width // width_break)
                    # Add more dummy nodes to simulate full tree if node isn't a leaf
                    if level != height:
                        node_queue.add(None)

            # Increase number of nodes processed
            node_count += 1

        return out
        
    # Iterator Accessors
    def inorder(self):
        """Return an iterator that performed an inorder traversal of self."""
        temp = []
        def recurse(node):
            if node:
                recurse(node.left)
                temp.append(node.data)
                recurse(node.right)
        recurse(self.root)
        return iter(temp)
    
    def levelorder(self):
        """Return an iterator that performed an levelorder traversal of self."""
        nodes_to_visit = DoublyLinkedQueue([self.root])
        temp = []
        while not nodes_to_visit.is_empty():
            node = nodes_to_visit.pop()
            temp.append(node.data)
            if node.left:
                nodes_to_visit.add(node.left)
            if node.right:
                nodes_to_visit.add(node.right)
        return iter(temp)
    
    def postorder(self):
        """Return an iterator that performed an postorder traversal of self."""
        temp = []
        def recurse(node):
            if node:
                recurse(node.left)
                recurse(node.right)
                temp.append(node.data)
        recurse(self.root)
        return iter(temp)
    
    def preorder(self):
        """Return an iterator that performed an preorder traversal of self."""
        temp = []
        node_stack = DoublyLinkedStack([self.root])
        
        def recurse(node):
            if node:
                temp.append(node.data)
                recurse(node.left)
                recurse(node.right)
        
        recurse(self.root)
        return iter(temp)

    # Mutators
    def add(self, item):
        """Add item to self, increment length."""

        # Check preconditions
        try:
            item < item
        except TypeError:
            raise TypeError("Cannot add non-comparable object to BST")

        if not self.is_empty():
            try:
                item < self.root.data
            except TypeError:
                msg = "Cannot add item that doesn't support comparison "
                msg += "with items currently in BST."
                raise TypeError(msg)
        
        # Helper recursion function
        def recurse(node):
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    return recurse(node.left)
            elif item > node.data:
                if node.right == None:
                    node.right = BSTNode(item)
                else:
                    return recurse(node.right)
            else:
                return False

        if self.is_empty():
            self.root = BSTNode(item)
            self.length += 1
        else:
            insertion_made = recurse(self.root)
            if insertion_made is None:
                self.length += 1
                
            

    def clear(self):
        """Remove all items from self, set length to 0."""
        self.length = 0
        self.root = None

    def remove(self, item):
        """
        Remove item from self, decrement length.
        Precondition: Item must be in self.
        Raises: LookupError
        """
        # Check precondition
        if item not in self:
            raise LookupError("Cannot remove item that is not in self.")

        # Recursive function to find target node and its parent
        def recurse(node, parent, link):
            if item == node.data:
                return node, parent, link
            elif item < node.data:
                return recurse(node.left, node, 'l')
            else:
                return recurse(node.right, node, 'r')
            
        # Find target node and its parent
        node, parent, link = recurse(self.root, self.root, '')

        # If target node has two children, replace with the largest value in the left
        # subtree and delete that value from the left subtree
        if node.left and node.right:
            lmax_node = node.left
            lmax_parent = node
            while lmax_node.right:
                lmax_parent = lmax_node
                lmax_node = lmax_node.right
            # Target node now has value of largest value in its left subtree
            node.data = lmax_node.data

            # If max child was target node's left, then max child has no right
            # Therefore just change target node's left child to be max node's left child
            if lmax_node.left and lmax_node is node.left:
                node.left = lmax_node.left
            # Elif max child has a left but max child is not target node's left.
            # Therefore make max node's parent's right point to max node's left. 
            elif lmax_node.left and lmax_node is not node.left:
                lmax_parent.right = lmax_node.left
            # There is no left to take max node's place, so parent's right points to
            # None
            else:
                lmax_parent.right = None
                
        # If target node only has left child, point parent's old connection toward
        # node's left child.
        elif node.left:
            if link == 'l':
                parent.left = node.left
            elif link == 'r':
                parent.right = node.left
            # Target node is root
            else:
                self.root = node.left
                
        # If target node only has right child, point parent's old connection toward
        # node's right child.
        elif node.right:
            if link == 'l':
                parent.left = node.right
            elif link == 'r':
                parent.right = node.right
            # Target node is root
            else:
                self.root = node.right
                
        # Target node is a leaf and can be removed
        else:
            if link == 'l':
                parent.left = None
            elif link == 'r':
                parent.right = None
            # Target node is singleton root
            else:
                self.root = None

        # Decrement length
        self.length -= 1
