"""
Author:  Russell Gerhard
Purpose: Create a unit testing framework for the methods implemented in all
         concrete classes that implement the binary search tree (BST) ADT.

Exports:
    TestConcreteBST: Test all methods provided by a concrete class implementing
                     a BST.
                     
    TestLinkedBST: Test all methods in and inherited by the LinkedBST
                   implementation.
"""

from binarysearchtrees import LinkedBST
from abstractcollectiontest import TestAbstractCollection
import unittest

class TestConcreteBST(TestAbstractCollection):

    # Constructor test
    def test_constructor(self):
        a = self.class_type()
        self.assertTrue(a.root is None)
        self.assertTrue(repr(a) == "LinkedBST()")
        a = self.class_type([4,2,1,3,6,5,7])
        self.assertTrue(a.root.data == 4)
        self.assertTrue(a.root.left.data == 2)
        self.assertTrue(a.root.left.left.data == 1)
        self.assertTrue(a.root.left.right.data == 3)
        self.assertTrue(a.root.right.data == 6)
        self.assertTrue(a.root.right.left.data == 5)
        self.assertTrue(a.root.right.right.data == 7)
        self.assertTrue(len(a) == 7)

    # Accessor tests
    def test_find(self):
        a = self.class_type([4,2,6,1,3])
        self.assertTrue(a.find(5) is None)
        self.assertTrue(a.find(4) == 4)

    def test_get_height(self):
        a = self.class_type()
        self.assertTrue(a.get_height() == 0)
        a.add(8)
        self.assertTrue(a.get_height() == 1)
        a.add(7)
        self.assertTrue(a.get_height() == 2)
        a.add(9)
        self.assertTrue(a.get_height() == 2)
        a.add(6)
        self.assertTrue(a.get_height() == 3)

    def test_iteration(self):
        preorder_list = [4,2,1,3,6,5,7]
        a = self.class_type(preorder_list)
        for i,item in enumerate(a):
            self.assertTrue(item == preorder_list[i])

    def test_repr(self):
        preorder_list = [8,4,2,1,3,6,5,7,12,10,9,11,14,13,15]
        a = self.class_type(preorder_list)
        tree_repr = f"{self.class_type.__name__}"
        tree_repr += "(8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15)"
        self.assertTrue(repr(a) == tree_repr)

    def test_str(self):
        tree_str = "               8                \n\n       4               12       \n\n   2               10      13   \n\n 1   3           9   11      15 \n\n                                "
        a = self.class_type([8,4,2,1,3,12,10,9,11,13,15])
        self.assertTrue(str(a) == tree_str)

    # Iterator Accessor tests
    def test_inorder(self):
        a = self.class_type([4,2,1,3,6,5,7])
        out = ''
        for item in a.inorder():
            out += str(item)
        self.assertTrue(out == "1234567")

    def test_levelorder(self):
        a = self.class_type([4,2,1,3,6,5,7])
        out = ''
        for item in a.levelorder():
            out += str(item)
        self.assertTrue(out == "4261357")

    def test_postorder(self):
        a = self.class_type([4,2,1,3,6,5,7])
        out = ''
        for item in a.postorder():
            out += str(item)
        self.assertTrue(out == "1325764")

    def test_preorder(self):
        a = self.class_type([4,2,1,3,6,5,7])
        out = ''
        for item in a.preorder():
            out += str(item)
        self.assertTrue(out == "4213657")

    # Mutator tests
    def test_add(self):
        b = self.class_type()
        with self.assertRaises(TypeError):
            b.add({})
        b.add(100)
        with self.assertRaises(TypeError):
            b.add('a')

        a = self.class_type()
        a.add(16)
        a.add(8)
        a.add(24)
        a.add(4)
        a.add(12)
        a.add(20)
        a.add(28)
        a.add(16)
        a.add(8)
        self.assertTrue(len(a) == 7)
        self.assertTrue(a.get_height() == 3)
        self.assertTrue(a.root.data == 16)
        self.assertTrue(a.root.left.data == 8)
        self.assertTrue(a.root.right.data == 24)
        self.assertTrue(a.root.right.right.data == 28)
        self.assertTrue(a.root.right.left.data == 20)
        self.assertTrue(a.root.left.right.data == 12)
        self.assertTrue(a.root.left.left.data == 4)
        
    def test_clear(self):
        a = self.class_type([1,2,3,7,5,4])
        self.assertFalse(a.is_empty())
        self.assertFalse(a.root is None)
        a.clear()
        self.assertTrue(a.is_empty())
        self.assertTrue(a.root is None)

    def test_remove(self):
        # Remove from empty
        a = self.class_type()
        with self.assertRaises(LookupError):
            a.remove(0)

        # Remove nonexistant
        a = self.class_type([2,1,3])
        with self.assertRaises(LookupError):
            a.remove(4)

        # Remove root
        a = self.class_type([16,8,4,12,24,20,28])
        self.assertTrue(len(a) == 7)
        a.remove(16)
        self.assertTrue(16 not in a)
        self.assertTrue(len(a) == 6)
        self.assertTrue(a.root.data == 12)
        self.assertTrue(a.root.left.right is None)

        # Remove leaf
        a.remove(4)
        self.assertTrue(4 not in a)
        self.assertTrue(len(a) == 5)
        self.assertTrue(a.root.left.left is None)

        # Remove node that only has right child
        a.add(7)
        a.remove(8)
        self.assertTrue(8 not in a)
        self.assertTrue(len(a) == 5)
        self.assertTrue(a.root.left.data == 7)

        # Remove node that only has left child
        a.add(9)
        a.remove(7)
        self.assertTrue(7 not in a)
        self.assertTrue(len(a) == 5)
        self.assertTrue(a.root.left.data == 9)
        
        # Remove node with 2 children
        # (replace with max in left subtree of node, max has no children)
        a = self.class_type([16,8,4,2,6,12,10,14,24,20,22,18,28,26,30])
        self.assertTrue(a.root.right.data == 24)
        a.remove(24)
        self.assertTrue(a.root.right.data == 22)
        self.assertTrue(24 not in a)
        self.assertTrue(len(a) == 14)

        # Remove node with 2 children (max has left child and is left of target node)
        a.add(17)
        a.remove(22)
        self.assertTrue(a.root.right.data == 20)
        self.assertTrue(22 not in a)
        self.assertTrue(len(a) == 14)
        self.assertTrue(a.root.right.left.data == 18)
        self.assertTrue(a.root.right.left.left.data == 17)

        # Remove node with 2 children (max has left child and is not left of target node)
        a.add(5)
        a.remove(8)
        self.assertTrue(a.root.left.data == 6)
        self.assertTrue(8 not in a)
        self.assertTrue(a.root.left.left.data == 4)
        self.assertTrue(a.root.left.left.right.data == 5)
        self.assertTrue(len(a) == 14)

        # Remove singleton root
        a = LinkedBST([1])
        a.remove(1)
        self.assertTrue(a.root is None)
        self.assertTrue(a.is_empty())

class TestLinkedBST(TestConcreteBST, unittest.TestCase):
    class_type = LinkedBST
        
        
        
                    
