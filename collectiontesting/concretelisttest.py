"""
Author:  Russell Gerhard
Purpose: Create a unit testing framework for the methods implemented in
         aall concrete classes that implement the list ADT.

Exports:
    TestConreteList: Test all methods provided by any concrete class
                     implementing a list.

    TestArrayList: Test all methods in and inherited by the ArrayList
                   implementation.

    TestLinkedList: Test all methods in and inherited by the LinkedList
                    implementation.

    TestDoublyLinkedList: Test all methods in and inherited by the
                          DoublyLinkedList implementation.
"""

from lists import ArrayList, LinkedList, DoublyLinkedList
from abstractlisttest import TestAbstractList
import unittest

class TestConcreteList(TestAbstractList):

    # Accessor tests
    def test_iterate(self):
        a = self.class_type([3,1,5,2,4])
        for i,item in enumerate(a):
            self.assertTrue(item == a[i])

    # Mutator tests
    def test_clear(self):
        a = self.class_type([2,4,1])
        a.clear()
        self.assertTrue(a.is_empty())
        a.clear()
        self.assertTrue(a.is_empty())

    def test_extend(self):
        a = self.class_type([6,4,'a'])
        a.extend([1,4,5,6])
        b = self.class_type([6,4,'a',1,4,5,6])
        self.assertTrue(a == b)

    def test_insert(self):
        a = self.class_type([1,'b'])
        a.insert(-1, 'a')
        a.insert(0, 10)
        a.insert(3, 20)
        a.insert(100, 'c')
        self.assertTrue(str(a) == "[10, a, 1, 20, b, c]")

    def test_pop(self):
        a = self.class_type([1,2,3,4])
        self.assertTrue(a.pop(2) == 3)
        self.assertTrue(a.pop() == 1)
        a.clear()
        with self.assertRaises(IndexError):
            a.pop()

    def test_remove(self):
        a = self.class_type([1,2,3,4])
        a.remove(2)
        a.remove(4)
        b = self.class_type([1,3])
        self.assertTrue(a == b)

    def test_reverse(self):
        a = self.class_type([1,2,3,4])
        b = self.class_type([4,3,2,1])
        a.reverse()
        self.assertTrue(a == b)

    def test_setitem(self):
        a = self.class_type([1,2,3,4])
        a[1] = 20
        a[3] = 40
        b = self.class_type([1,20,3,40])
        self.assertTrue(a == b)
        with self.assertRaises(IndexError):
            a[5] = 10

    def test_sort(self):
        a = self.class_type([4,6,2,1,5,3])
        a.sort()
        b = self.class_type([1,2,3,4,5,6])
        self.assertTrue(a == b)

class TestArrayList(TestConcreteList, unittest.TestCase):
    class_type = ArrayList

class TestLinkedList(TestConcreteList, unittest.TestCase):
    class_type = LinkedList

class TestDoublyLinkedList(TestConcreteList, unittest.TestCase):
    class_type = DoublyLinkedList
