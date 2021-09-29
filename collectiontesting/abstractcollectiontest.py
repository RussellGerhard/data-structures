"""
Author:  Russell Gerhard
Purpose: Create unit testing framework for the methods implemented in
         the AbstractCollection class. This testing class is meant to be
         inherited by other testing classes, much like AbstractCollection is
         meant to be inherited. It would make as much sense to run these tests
         as it would to instantiate AbstractCollection (very little).

Exports:
    TestAbstractCollection: Test all methods provided by the AbstractCollection
                            class.
"""

class TestAbstractCollection():
    
    # Accessor tests
    def test_concatentation(self):
        # Different types
        a = self.class_type()
        b = [0, 1, 2]
        with self.assertRaises(TypeError):
            a + b

        # Both empty
        a = self.class_type()
        b = self.class_type()
        c = a + b
        self.assertTrue(a == b == c)

        # One empty
        a = self.class_type()
        b = self.class_type(['a', 'c', 'b'])
        c = a + b
        self.assertTrue(b == c)
        
        # Both nonempty
        a = self.class_type(['a', 'b'])
        b = self.class_type(['c', 'd'])
        c = self.class_type(['a', 'b', 'c', 'd'])
        d = a + b
        self.assertTrue(c == d)

    def test_containment(self):
        # Item not in collection
        a = self.class_type()
        self.assertFalse(1 in a)

        # Item in collection
        a = self.class_type([1,3,2])
        self.assertTrue(2 in a)

    def test_copy(self):
        # Empty
        a = self.class_type()
        b = a.copy()
        self.assertTrue(b.is_empty())
        self.assertTrue(b == a)
        self.assertTrue(b is not a)

        # Nonempty
        a = self.class_type([4,32,6,1])
        b = a.copy()
        self.assertFalse(b.is_empty())
        self.assertTrue(b == a)
        self.assertTrue(b is not a)

    def test_count(self):
        # Empty
        a = self.class_type()
        self.assertTrue(a.count(1) == 0)

        # Nonempty, not instances
        a = self.class_type([3,1,2,3])
        self.assertTrue(a.count(4) == 0)

        # Nonempty, one instance
        a = self.class_type([3,1,2,3])
        self.assertTrue(a.count(2) == 1)

    def test_equality(self):
        # Same object
        a = self.class_type()
        b = a
        self.assertTrue(a == b)

        # Different types
        a = self.class_type()
        self.assertFalse(a == 'hello')

        # Different lengths
        a = self.class_type([1,2])
        b = self.class_type([1,2,3])
        self.assertFalse(a == b)

        # Both empty
        a = self.class_type()
        b = self.class_type()
        self.assertTrue(a == b)

        # Both nonempty
        a = self.class_type([1,2,3,4,5])
        b = self.class_type([1,2,3,4,5])
        self.assertTrue(a == b)

    def test_is_empty(self):
        # Is empty
        a = self.class_type()
        self.assertTrue(a.is_empty())

        # Isn't empty
        a = self.class_type([1,2])
        self.assertFalse(a.is_empty())

    def test_len(self):
        # Empty
        a = self.class_type()
        self.assertTrue(len(a) == 0)

        # Nonempty
        a = self.class_type([1,3,2])
        self.assertTrue(len(a) == 3)

    def test_repr(self):
        # Empty
        a = self.class_type()
        self.assertTrue(repr(a) == f"{self.class_type.__name__}()")

        # Nonempty
        a = self.class_type([5,2,3,'b'])
        self.assertTrue(repr(a) == f"{self.class_type.__name__}(5, 2, 3, b)")

    def test_str(self):
        # Empty
        a = self.class_type()
        self.assertTrue(str(a) == "[]")

        # Nonempty
        a = self.class_type([5,2,3,'b'])
        self.assertTrue(str(a) == "[5, 2, 3, b]")
