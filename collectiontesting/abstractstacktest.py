"""
Author:  Russell Gerhard
Purpose: Create a unit testing framework for all methods implemented by the
         AstractStack class. This testing class is meant to be inherited, much
         like AbstractStack is meant to be inherited.

Exports:
    TestAbstractStack: Test all methods provided in AbstractStack class.
"""

from abstractcollectiontest import TestAbstractCollection

class TestAbstractStack(TestAbstractCollection):

    # Accessor tests
    def test_add(self):
        a = self.class_type()
        a.add('a')
        a.add(2)
        a.add(78)
        self.assertTrue(str(a) == "[a | 2 | 78]")

    def test_str(self):
        a = self.class_type()
        self.assertTrue(str(a) == "[]")
        a = self.class_type([1,5,6,'a',[],90,'baba'])
        self.assertTrue(str(a) == "[1 | 5 | 6 | a | [] | 90 | baba]")
