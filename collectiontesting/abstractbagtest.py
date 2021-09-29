"""
Author:  Russell Gerhard
Purpose: Create unit testing framework for the methods implemented in
         the AbstractBag class. This testing class is meant to be
         inherited by other testing classes, much like AbstractBag is
         meant to be inherited. It would make as much sense to run these tests
         as it would to instantiate AbstractBag (very little).

Exports:
    TestAbstractBag: Test all methods povided by the AbstractBag class.
"""

from abstractcollectiontest import TestAbstractCollection

class TestAbstractBag(TestAbstractCollection):

    # Accessor Tests
    # Sorted and unsorted equality
    def test_equality_unordered(self):
        a = self.class_type([1,2,3,4,5])
        b = self.class_type([5,4,3,2,1])
        self.assertTrue(a == b)

    def test_str(self):
        # Empty
        a = self.class_type()
        self.assertTrue(str(a) == "{}")

        # Nonempty
        a = self.class_type([1,5,2,3])
        self.assertTrue(str(a) == "{1, 5, 2, 3}")
