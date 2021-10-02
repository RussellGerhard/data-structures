"""
Author:  Russell Gerhard
Purpose: Create unit testing framework for the methods implemented in
         the AbstractList class. This testing class is meant to be
         inherited by other testing classes, much like AbstractList is
         meant to be inherited. It would make as much sense to run these tests
         as it would to instantiate AbstractList (very little).

Exports:
    TestAbstractList: Test all methods provided by the AbstractList class.
"""

from abstractcollectiontest import TestAbstractCollection

class TestAbstractList(TestAbstractCollection):

    # Accessor tests
    def test_getitem(self):
        # Out of range, empty
        a = self.class_type()
        with self.assertRaises(IndexError):
            b = a[0]
            
        # Out of range, nonempty
        a = self.class_type([1,2])
        with self.assertRaises(IndexError):
            b = a[3]
            
        # Functioning __getitem__ calls
        a = self.class_type([1,2])
        self.assertTrue(a[0] == 1)
        self.assertTrue(a[1] == 2)

    def test_index(self):
        a = self.class_type([1,3,2])
        self.assertTrue(a.index(4) == -1)
        self.assertTrue(a.index(3) == 1)

    # Mutator tests
    def test_add(self):
        a = self.class_type()
        a.add(1)
        a.add(2)
        self.assertTrue(a[0] == 1)
        self.assertTrue(a[1] == 2)

    def test_append(self):
        a = self.class_type()
        a.append(1)
        a.append(2)
        self.assertTrue(a[0] == 1)
        self.assertTrue(a[1] == 2)

    def test_prepend(self):
        a = self.class_type()
        a.prepend(1)
        a.prepend(2)
        self.assertTrue(a[0] == 2)
        self.assertTrue(a[1] == 1)

    def test_remove(self):
        a = self.class_type([1,2,3,4])
        a.remove(2)
        a.remove(4)
        b = self.class_type([1,3])
        self.assertTrue(a == b)
