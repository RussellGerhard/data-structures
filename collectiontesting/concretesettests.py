"""
Author:  Russell Gerhard
Purpose: Create a unit testing framework for the methods implemented in all
         concrete classes that implement the set ADT.

Exports:
    TestArraySet: Test all methods in and inherited by the ArraySet
                  implementation of the set ADT.

    TestArraySortetSet: Test all methods in and inherited by the ArraySortedSet
                        implementation of a sorted set.
                        

    TestLinkedSet: Test all methods in and inherited by the LinkedSet
                   implementation of the set ADT.
"""

from concretebagtests import TestArrayBag, TestArraySortedBag, TestLinkedBag
from sets import ArraySet, ArraySortedSet, LinkedSet
import unittest

class TestArraySet(TestArrayBag):
    class_type = ArraySet

    # Constructor tests
    def test_constructor(self):
        a = self.class_type([1,4,5,1,2,3,'a','a','b',6,6,'c'])
        self.assertTrue(str(a) == "{1, 4, 5, 2, 3, a, b, 6, c}")
        a = self.class_type()
        self.assertTrue(str(a) == "{}")

    # Accessor tests
    def test_iterate(self):
        a = self.class_type([1,'c','c',2,5,4,2,5,'b'])
        l = [1,'c',2,5,4,'b']
        for i,item in enumerate(a):
            self.assertTrue(l[i] == item)

    # Mutator tests
    def test_add(self):
        a = self.class_type()
        a.add(1)
        a.add(2)
        a.add(1)
        a.add('a')
        a.add('b')
        a.add('a')
        a.add(3)
        a.add(2)
        self.assertTrue(len(a) == 5)
        self.assertTrue(str(a) == "{1, 2, a, b, 3}")

    def test_remove(self):
        a = self.class_type([1,1,6,7])
        a.remove(1)
        self.assertTrue(str(a) == "{6, 7}")
        a.remove(7)
        self.assertTrue(str(a) == "{6}")
    

class TestArraySortedSet(TestArraySortedBag):
    class_type = ArraySortedSet

    # Constructor tests
    def test_constructor(self):
        a = self.class_type([1,4,5,1,2,3,6,6])
        self.assertTrue(str(a) == "{1, 2, 3, 4, 5, 6}")
        a = self.class_type()
        self.assertTrue(str(a) == "{}")

    # Accessor tests
    def test_iterate(self):
        a = self.class_type([1,2,5,4,2,5])
        l = [1,2,4,5]
        for i,item in enumerate(a):
            self.assertTrue(l[i] == item)

    # Mutator tests
    def test_add(self):
        a = self.class_type()
        a.add(1)
        a.add(2)
        a.add(1)
        with self.assertRaises(TypeError):
            a.add({})
        with self.assertRaises(TypeError):
            a.add('a')
        a.add(3)
        a.add(2)
        a.add(0)
        a.add(0)
        a.add(2.5)
        self.assertTrue(len(a) == 5)
        self.assertTrue(str(a) == "{0, 1, 2, 2.5, 3}")

    def test_remove(self):
        a = self.class_type([1,1,6,7])
        a.remove(1)
        self.assertTrue(str(a) == "{6, 7}")
        a.remove(7)
        self.assertTrue(str(a) == "{6}")
        

class TestLinkedSet(TestLinkedBag):
    class_type = LinkedSet

    # Constructor tests
    def test_constructor(self):
        a = self.class_type([1,4,5,1,2,3,'a','a','b',6,6,'c'])
        self.assertTrue(str(a) == "{1, 4, 5, 2, 3, a, b, 6, c}")
        a = self.class_type()
        self.assertTrue(str(a) == "{}")

    # Accessor tests
    def test_iterate(self):
        a = self.class_type([1,'c','c',2,5,4,2,5,'b'])
        l = [1,'c',2,5,4,'b']
        for i,item in enumerate(a):
            self.assertTrue(l[i] == item)

    # Mutator tests
    def test_add(self):
        a = self.class_type()
        a.add(1)
        a.add(2)
        a.add(1)
        a.add('a')
        a.add('b')
        a.add('a')
        a.add(3)
        a.add(2)
        self.assertTrue(len(a) == 5)
        self.assertTrue(str(a) == "{1, 2, a, b, 3}")

    def test_remove(self):
        a = self.class_type([1,1,6,7])
        a.remove(1)
        self.assertTrue(str(a) == "{6, 7}")
        a.remove(7)
        self.assertTrue(str(a) == "{6}")
