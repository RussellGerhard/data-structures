"""
Author:  Russell Gerhard
Purpose: Create a unit testing framework for any class implementing the heap
         abstract data type.

Exports:
    TestConcreteHeap: Test all methods provided by concrete class implementing
                      a heap.

    TestArrayHeap: Test all methods implemented in and inherited by the
                   ArrayHeap implementation.
"""

from heaps import ArrayHeap
from abstractcollectiontest import TestAbstractCollection
import unittest

class TestConcreteHeap(TestAbstractCollection):

    # Constructor test
    def test_constructor(self):
        a = self.class_type()
        self.assertTrue(a.is_empty())
        self.assertTrue(repr(a) == "ArrayHeap()")
        a = self.class_type([4,1,6,12,12,73,3,13,14,11,11])
        repr_val = "ArrayHeap(1, 4, 3, 12, 11, 73, 6, 13, 14, 12, 11)"
        self.assertTrue(repr(a) == repr_val)

    # Accessor tests
    def test_equality(self):
        a = self.class_type([9,7,2,5,1,1,5,10,11,4])
        b = self.class_type([1,5,10,11,9,1,7,2,5,4])
        self.assertTrue(a == b)
        a.add(1)
        b.add(2)
        self.assertFalse(a == b)

    def test_iteration(self):
        a = self.class_type([2,4,1,6,23,10,11,14])
        for i,item in enumerate(a):
            self.assertTrue(item == a.items[i])

    def test_peek(self):
        a = self.class_type()
        with self.assertRaises(LookupError):
            a.peek()
        a.add(1)
        self.assertTrue(a.peek() == 1)
        self.assertTrue(a.peek() == 1)
        a.add(0)
        self.assertTrue(a.peek() == 0)

    def test_repr(self):
        a = self.class_type()
        self.assertTrue(repr(a) == "ArrayHeap()")
        a.add(4)
        a.add(2)
        a.add(5)
        a.add(1)
        self.assertTrue(repr(a) == "ArrayHeap(1, 2, 5, 4)")

    def test_str(self):
        a = self.class_type([1,3,1,5,7,2,3,8,9])
        heap_str = "               1                \n\n       3               1        \n\n   5       7       2       3    \n\n 8   9  "
        self.assertTrue(str(a) == heap_str)
        a = self.class_type()
        self.assertTrue(str(a) == '')
    
    # Mutator tests
    def test_add(self):
        a = self.class_type()
        a.add(10)
        a.add(3)
        a.add(5)
        a.add(5)
        a.add(5)
        a.add(1)
        a.add(12)
        a.add(11)
        a.add(10)
        self.assertTrue(repr(a) == "ArrayHeap(1, 5, 3, 10, 5, 5, 12, 11, 10)")

    def test_clear(self):
        a = self.class_type()
        a.clear()
        self.assertTrue(a.is_empty())
        a = self.class_type([4,3,2,5,1,6])
        a.clear()
        self.assertTrue(a.is_empty())

    def test_remove(self):
        a = self.class_type([1,5,3,10,5,5,12,11,10])
        self.assertTrue(a.pop() == 1)
        self.assertTrue(repr(a) == "ArrayHeap(3, 5, 5, 10, 5, 10, 12, 11)")
        self.assertTrue(a.pop() == 3)
        self.assertTrue(repr(a) == "ArrayHeap(5, 5, 5, 10, 11, 10, 12)")
        self.assertTrue(a.pop() == 5)
        self.assertTrue(repr(a) == "ArrayHeap(5, 10, 5, 12, 11, 10)")
        self.assertTrue(a.pop() == 5)
        self.assertTrue(repr(a) == "ArrayHeap(5, 10, 10, 12, 11)")
        self.assertTrue(a.pop() == 5)
        self.assertTrue(repr(a) == "ArrayHeap(10, 11, 10, 12)")
        self.assertTrue(a.pop() == 10)
        self.assertTrue(repr(a) == "ArrayHeap(10, 11, 12)")
        self.assertTrue(a.pop() == 10)
        self.assertTrue(repr(a) == "ArrayHeap(11, 12)")
        self.assertTrue(a.pop() == 11)
        self.assertTrue(repr(a) == "ArrayHeap(12)")
        self.assertTrue(a.pop() == 12)
        self.assertTrue(repr(a) == "ArrayHeap()")
        self.assertTrue(a.is_empty())
        with self.assertRaises(LookupError):
            a.pop()

class TestArrayHeap(TestConcreteHeap, unittest.TestCase):
    class_type = ArrayHeap
