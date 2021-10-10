"""
Author:  Russell Gerhard
Purpose: Unit test any methods in or inherited by a class implementing the
         dictionary ADT.

Exports:
    TestConcreteDict: Provide tests for any methods implemented in a concrete
                      dictionary class.

    TestArrayDict: Test all methods in the dictionary interface as implemented
                   by the ArrayDict class.

    TestHashDict: Test all methods in the dictionary interface as implemented
                  by the HashDict class.
"""

from dicts import ArrayDict
from abstractdicttest import TestAbstractDict
import unittest

class TestConcreteDict(TestAbstractDict):

    # Constructor test
    def test_constructor(self):
        a = self.class_type()
        self.assertTrue(a.is_empty())
        with self.assertRaises(ValueError):
            a = self.class_type([1,2],['a'])
        a = self.class_type(['a', 'b', 'c'], [1,2,3])
        self.assertTrue(str(a) == "{'a': 1, 'b': 2, 'c': 3}")

    # Accessor tests
    def test_getitem(self):
        a = self.class_type(['one', 'two', 'three'], [1,2,3])
        self.assertTrue(a['one'] == 1)
        self.assertTrue(a['two'] == 2)
        self.assertTrue(a['three'] == 3)
        with self.assertRaises(KeyError):
            a['four']
        
    def test_iter(self):
        a = self.class_type(['a', 'b', 1, 43], ['red', 'blue', 'green', 'pink'])
        key_list = ['a', 'b', 1, 43]
        for key in a.keys():
            self.assertTrue(key in key_list)

    #Mutator tests
    def test_clear(self):
        a = self.class_type(['one', 'two', 'three'], [1,2,3])
        a.clear()
        self.assertTrue(a.is_empty())

    def test_pop(self):
        a = self.class_type(['one', 'two', 'three'], [1,2,3])
        self.assertTrue(a.pop('one', -1) == 1)
        self.assertTrue(a.pop('one', -1) == -1)
        self.assertTrue(a.pop('two', -1) == 2)
        self.assertTrue(a.pop('two', -1) == -1)
        self.assertTrue(a.pop('three', -1) == 3)
        self.assertTrue(a.pop('three', -1) == -1)
        self.assertTrue(a.is_empty())
        self.assertTrue(a.pop('four', -1) == -1)

    def test_setitem(self):
        a = self.class_type(['one', 'two', 'three'], [1,2,3])
        a['one'] = 11
        self.assertTrue(a.get('one', -1) == 11)
        a['two'] = 22
        self.assertTrue(a.get('two', -1) == 22)
        a['four'] = 4
        self.assertTrue(a.get('four', -1) == 4)
        a['four'] = 44
        self.assertTrue(a.get('four', -1) == 44)

class TestArrayDict(TestConcreteDict, unittest.TestCase):
    class_type = ArrayDict

class TestHashDict(TestConcreteDict, unittest.TestCase):
    class_type = HashDict
        
        
