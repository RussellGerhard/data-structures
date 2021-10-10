"""
Author:  Russell Gerhard
Purpose: Create unit testing framework for the methods implemented in the
         AbstractDict class. This testing class is a base class.

Exports:
    TestAbstractDict: Test all methods provided by the AbstractDict class.
"""

from abstractcollectiontest import TestAbstractCollection

class TestAbstractDict(TestAbstractCollection):

    # Accessor tests
    def test_concatenation(self):
        a = self.class_type()
        b = {}
        with self.assertRaises(TypeError):
            a + b
        a = self.class_type()
        b = self.class_type()
        d = a + b
        self.assertTrue(a == d)
        self.assertTrue(d.is_empty())
        a = self.class_type(['a', 'b', 'c'], [1,2,3])
        b = self.class_type(['d', 'e'], [3, 4])
        c = self.class_type(['a', 'b', 'c', 'd', 'e'], [1,2,3,3,4])
        d = a + b
        self.assertTrue(c == d)
        
    def test_contains(self):
        a = self.class_type()
        self.assertFalse('a' in a)
        a = self.class_type(['a', 'b'], ['c', 'd'])
        self.assertTrue('a' in a)
        self.assertFalse('c' in a)

    def test_copy(self):
        a = self.class_type()
        b = a.copy()
        self.assertFalse(a is b)
        self.assertTrue(a == b)
        self.assertTrue(b.is_empty())
        a = self.class_type([1,2], ['a', 'b'])
        b = a.copy()
        self.assertFalse(a is b)
        self.assertTrue(a == b)

    def test_count(self):
        a = self.class_type()
        self.assertTrue(a.count(1) == 0)
        a = self.class_type(['a', 'b', 'c'], [1,2,1])
        self.assertTrue(a.count(1) == 2)
        self.assertTrue(a.count(2) == 1)
        self.assertTrue(a.count(3) == 0)

    def test_entries(self):
        a = self.class_type(['a', 'b', 1, 43], ['red', 'blue', 'green', 'pink'])
        for entry in a.entries():
            self.assertTrue(a[entry.key] == entry.value)

    def test_equality(self):
        a = self.class_type()
        b = self.class_type()
        self.assertTrue(a == b)
        a = self.class_type(['a', 'b', 1, 43], ['red', 'blue', 'green', 'pink'])
        b = self.class_type(['a', 'b', 1, 43], ['red', 'blue', 'green', 'pink'])
        self.assertTrue(a == b)
        a = self.class_type(['a', 'b', 1], ['red', 'blue', 'green'])
        b = self.class_type(['a', 'b', 1, 43], ['red', 'blue', 'green', 'pink'])
        self.assertFalse(a == b)

    def test_get(self):
        a = self.class_type()
        self.assertTrue(a.get('a', -1) == -1)
        a = self.class_type(['a'], [1])
        self.assertTrue(a.get('a', -1) == 1)
        self.assertTrue(a.get('b', -1) == -1)

    def test_is_empty(self):
        # Is empty
        a = self.class_type()
        self.assertTrue(a.is_empty())

        # Isn't empty
        a = self.class_type(['a','b'], [1,2])
        self.assertFalse(a.is_empty())

    def test_keys(self):
        a = self.class_type(['a', 'b', 1, 43], ['red', 'blue', 'green', 'pink'])
        key_list = ['a', 'b', 1, 43]
        for key in a.keys():
            self.assertTrue(key in key_list)

    def test_len(self):
        # Empty
        a = self.class_type()
        self.assertTrue(len(a) == 0)

        # Nonempty
        a = self.class_type(['a','b','c'], [1,3,2])
        self.assertTrue(len(a) == 3)

    def test_repr(self):
        a = self.class_type()
        self.assertTrue(repr(a) == f"{self.class_type.__name__}()")
        a = self.class_type([1,2,3], [4,5,6])
        repr_str = f"{self.class_type.__name__}(1: 4, 2: 5, 3: 6)"
        self.assertTrue(repr(a) == repr_str)
        a = self.class_type(['a','b','c'], [1,2,3])
        repr_str = f"{self.class_type.__name__}('a': 1, 'b': 2, 'c': 3)"
        self.assertTrue(repr(a) == repr_str)

    def test_str(self):
        a = self.class_type()
        self.assertTrue(str(a) == "{}")
        a = self.class_type([1,2,3], [4,5,6])
        self.assertTrue(str(a) == "{1: 4, 2: 5, 3: 6}")
        a = self.class_type(['a','b','c'], [1,2,3])
        self.assertTrue(str(a) == "{'a': 1, 'b': 2, 'c': 3}")

    def test_values(self):
        a = self.class_type(['a', 'b', 1, 43], ['red', 'blue', 'green', 'pink'])
        value_list = ['red', 'blue', 'green', 'pink']
        for value in a.values():
            self.assertTrue(value in value_list)
            
