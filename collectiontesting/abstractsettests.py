"""
Author:  Russell Gerhard
Purpose: Create unit testing framework for the methods implemented in the
         AbstractSet class. This testing class is meant to be a base class.

Exports:
    TestAbstractSet: Test all methods provided by the AbstractSet class.
"""

class TestAbstractSet:

    # Accessor tests
    def test_difference(self):
        a = self.class_type()
        b = self.class_type()
        d = a - b
        self.assertTrue(a == d)
        a = self.class_type([1,2,3,4,5])
        b = self.class_type([1,3,5])
        c = self.class_type([2,4])
        d = a - b
        self.assertTrue(c == d)
        
    def test_intersection(self):
        a = self.class_type()
        b = self.class_type()
        d = a & b
        self.assertTrue(a == d)
        a = self.class_type([1,5,3,3,4])
        b = self.class_type([3,4,2,2])
        c = self.class_type([3,4])
        d = a & b
        self.assertTrue(c == d)

    def test_is_subset(self):
        a = self.class_type()
        b = self.class_type()
        self.assertTrue(a.is_subset(b))
        a = self.class_type([1,2,3])
        b = self.class_type([1,2,3,4])
        self.assertTrue(a.is_subset(b))
        self.assertFalse(b.is_subset(a))

    def test_union(self):
        a = self.class_type()
        b = self.class_type()
        d = a | b
        self.assertTrue(a == d)
        a = self.class_type([1,3,5])
        b = self.class_type([2,4,6])
        c = self.class_type([1,2,3,4,5,6])
        d = a | b
        self.assertTrue(c == d)
