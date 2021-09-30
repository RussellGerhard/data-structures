"""
Author:  Russell Gerhard
Purpose: Create a unit testing framework for the methos implemented in all
         concrete classes that implement the list ADT.

Exports:
    TestConcreteStack: Test all methods provided by any concrete class
                       implementing the stack ADT. Meant to be inherited.

    TestArrayStack: Test all methods in and inherited by the ArrayStack
                    implementation of the stack ADT.

    TestDoublyLinkedStack: Test all methods in and inherited by the
                           DoublyLinkedStack implementation of the stack ADT.
"""

from abstractstacktest import TestAbstractStack
from stacks import ArrayStack, DoublyLinkedStack
import unittest

def TestConcreteStack(TestAbstractStack):

    # Constructor test
    def test_constructor(self):
        a = self.class_type()
        self.assertTrue(str(a) == "[]")
        a = self.class_type([5,'a',3,9,'b',9])
        self.assertTrue(str(a) == "[5 | a | 3 | 9 | b | 9]")

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
        self.assertTrue(a.peek() == 'a')
        a.pop()
        self.assertTrue(a.peek() == 2)

    # Mutator tests
    def test_clear(self):
        a = self.class_type([2,1,2,'a','b',3])
        a.clear()
        self.assertTrue(self.is_empty())

    def test_pop(self):
        a = self.class_type([5,1,'a'])
        self.assertTrue(a.pop() == a)
        self.assertTrue(a.pop() == 1)
        self.assertTrue(a.pop() == 5)
        self.assertTrue(a.is_empty())
        with self.assertRaises(LookupError):
            a.pop()

    def test_push(self):
        a = self.class_type()
        a.push('a')
        a.push(1)
        a.push(24)
        a.push(['a'])
        self.assertTrue(str(a) == "[a | 1 | 24 | 24 | [a]]")
        
