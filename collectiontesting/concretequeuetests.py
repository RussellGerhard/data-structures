"""
Author:  Russell Gerhard
Purpose: Create a unit testing framework for the methos implemented in all
         concrete classes that implement the queue ADT.

Exports:
    TestConcreteQueue: Test all methods provided by any concrete class
                       implementing the queue ADT. Meant to be inherited.

    TestArrayQueue: Test all methods in and inherited by the ArrayQueue
                    implementation of the queue ADT.

    TestDoublyLinkedQueue: Test all methods in and inherited by the
                           DoublyLinkedQueue implementation of the queue ADT.
"""

from abstractcollectiontest import TestAbstractCollection
from queues import ArrayQueue, DoublyLinkedQueue
import unittest

class TestConcreteQueue(TestAbstractCollection):

    # Constructor test
    def test_constructor(self):
        a = self.class_type()
        self.assertTrue(str(a) == "[]")
        a = self.class_type([5,'a',3,9,'b',9])
        self.assertTrue(str(a) == "[5, a, 3, 9, b, 9]")

    # Accessor tests
    def test_iterate(self):
        a = self.class_type([3,1,5,2,4,4])
        for i,item in enumerate(a):
            self.assertTrue(item == a.items[i])

    def test_peek(self):
        a = self.class_type()
        with self.assertRaises(LookupError):
            a.peek()
        a = self.class_type([4,1,2,'a'])
        self.assertTrue(a.peek() == 4)
        a.pop()
        self.assertTrue(a.peek() == 1)

    # Mutator tests
    def test_add(self):
        a = self.class_type()
        a.add('a')
        a.add(1)
        a.add(24)
        a.add(['a'])
        self.assertTrue(str(a) == "[a, 1, 24, ['a']]")
    
    def test_clear(self):
        a = self.class_type([2,1,2,'a','b',3])
        a.clear()
        self.assertTrue(a.is_empty())

    def test_pop(self):
        a = self.class_type([5,1,'a'])
        self.assertTrue(a.pop() == 5)
        self.assertTrue(a.pop() == 1)
        self.assertTrue(a.pop() == 'a')
        self.assertTrue(a.is_empty())
        with self.assertRaises(LookupError):
            a.pop()


class TestArrayQueue(TestConcreteQueue, unittest.TestCase):
    class_type = ArrayQueue
    

class TestDoublyLinkedQueue(TestConcreteQueue, unittest.TestCase):
    class_type = DoublyLinkedQueue
