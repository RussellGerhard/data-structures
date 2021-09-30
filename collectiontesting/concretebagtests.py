"""
Author:  Russell Gerhard
Purpose: Create a unit testing framework for the methods implemented in all
         concrete classes that implement the bag ADT.

Exports:
    TestConcreteBag: Test all methods provided by any concrete class
                     implementing a bag. Meant to be inherited.

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

    # Constructor tests
    def test_constructor(self):
        a = self.class_type([1,4,2,'a','b',3,2,1,'b'])
        self.assertTrue(str(a) == "{1, 4, 2, a, b, 3, 2, 1, b}")
        a = self.class_type()
        self.assertTrue(str(a) == "{}")
    
    # Accessor tests
    def test_iterate(self):
        a = self.class_type([1,'c','c',2,5,4,2,5,'b'])
        l = [1,'c','c',2,5,4,2,5,'b']
        for i,item in enumerate(a):
            self.assertTrue(l[i] == item)

    # Mutator tests
    def test_clear(self):
        a = self.class_type([1,1,4,4,4])
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
        self.assertTrue(len(a) == 4)
        self.assertTrue(str(a) == "{1, 2, 1, a}")

    def test_remove(self):
        a = self.class_type([1,1,6,7])
        a.remove(1)
        self.assertTrue(str(a) == "{1, 6, 7}")
        a.remove(7)
        self.assertTrue(str(a) == "{1, 6}")
        

class TestArrayBag(TestConcreteBag, unittest.TestCase):
    class_type = ArrayBag


class TestLinkedBag(TestConcreteBag, unittest.TestCase):
    class_type = LinkedBag
    

class TestArraySortedBag(TestConcreteBag, unittest.TestCase):
    class_type = ArraySortedBag

    # Constructor tests
    def test_constructor(self):
        a = self.class_type([1,4,2,3,2,1])
        self.assertTrue(str(a) == "{1, 1, 2, 2, 3, 4}")
        a = self.class_type()
        self.assertTrue(str(a) == "{}")

    # Accessor tests
    def test_iterate(self):
        a = self.class_type([1,2,5,4,2,5])
        l = [1,2,2,4,5,5]
        for i,item in enumerate(a):
            self.assertTrue(l[i] == item)

    def test_repr(self):
        a = self.class_type([6,1,4,2,3,5])
        self.assertTrue(repr(a) == f"{self.class_type.__name__}(1, 2, 3, 4, 5, 6)")

    def test_str(self):
        a = self.class_type([6,1,4,2,3,5])
        self.assertTrue(str(a) == "{1, 2, 3, 4, 5, 6}")

    # Mutator tests
    def test_add(self):
        a = self.class_type()
        a.add(9)
        a.add(4)
        with self.assertRaises(TypeError):
            a.add({'a':1})
        with self.assertRaises(TypeError):
            a.add('a')
        a.add(2)
        a.add(1)
        a.add(9)
        self.assertTrue(str(a) == "{1, 2, 4, 9, 9}")
        
