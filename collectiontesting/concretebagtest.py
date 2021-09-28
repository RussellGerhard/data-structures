"""
Author:  Russell Gerhard
Purpose: Create a unit testing framework for the methods implemented in all
         concrete classes that implement the bag ADT.

Exports:
    TestConcreteBag: Test all methods provided by any concrete class
                     implementing a bag.

    TestArrayBag: Test all methods in and inherited by the ArrayBag
                  implementation of the bag ADT.

    TestArraySortetBag: Test all methods in and inherited by the ArraySortedBag
                        implementation of a sorted bag.
                        

    TestLinkedBag: Test all methods in and inherited by the LinkedBag
                   implementation of the bag ADT.
"""

from bags import ArrayBag, ArraySortedBag, LinkedBag
from abstractbagtest import TestAbstractBag
import unittest

class TestConcreteBag(TestAbstractBag):

    # Accessor tests
    # Iteration
    def test_unordered_equality(self):
        a = self.class_type([1,5,2,4,7,7,7,1])
        b = self.class_type([1,7,7,4,1,7,5,2])
        self.assertTrue(a == b)
    
    def test_iterate(self):
        a = self.class_type([1,'c','c',2,5,4,2,5,'b'])
        l = [1,'c','c',2,5,4,2,5,'b']
        for i,item in enumerate(a):
            self.assertTrue(l[i] == item)

    # Mutator tests
    def test_clear(self):
        a = self.class_type([1,1,4,4,4,'a'])
        b = self.class_type()
        a.clear()
        self.assertTrue(a.is_empty())
        self.assertTrue(a.position == -1)
        self.assertTrue(a == b)

    def test_add(self):
        a = self.class_type()
        a.add(1)
        a.add(2)
        a.add(1)
        a.add('a')
        self.assertTrue(a.length == 4)
        self.assertTrue(repr(a) == f"{self.class_type.__name__}(1, 2, 1, a)")

    def test_remove(self):
        a = self.class_type([1,1,6,7])
        a.remove(1)
        self.assertTrue(str(a) == "{1, 6, 7}")
        a.remove(7)
        self.assertTrue(str(a) == "{1, 6}")

class TestArrayBag(TestConcreteBag, unittest.TestCase):
    class_type = ArrayBag

class TestArraySortedBag(TestConcreteBag, unittest.TestCase):
    class_type = ArraySortedBag        
        
    def test_add(self):
        a = self.class_type()
        a.add(9)
        a.add(4)
        a.add(2)
        a.add(1)
        self.assertTrue(str(a) == "{1, 2, 4, 9}")

class TestLinkedBag(TestConcreteBag, unittest.TestCase):
    class_type = LinkedBag
        
