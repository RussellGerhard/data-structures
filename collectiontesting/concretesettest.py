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

from concretebagtest import TestArrayBag, TestArraySortedBag, TestLinkedBag

class TestConcreteSet:

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
    

class TestArraySet(TestArrayBag, TestConcreteSet):
    class_type = ArraySet

class TestArraySortedSet(TestArraySortedBag, TestConcreteSet):
    class_type = ArraySortedSet

class TestLinkedSet(TestLinkedBag, TestConcreteSet):
    class_type = LinkedSet

    
