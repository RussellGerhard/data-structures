"""
Author:  Russell Gerhard
Purpose: Create unit testing framework for the ArrayBag implementation
         of the bag abstract data type.
"""

from bags import ArrayBag
import unittest

# Accessor Tests
class TestConcatenation(unittest.TestCase):

    def test_concat_different_types(self):
        a = ArrayBag()
        b = [0,1,2]
        with self.assertRaises(TypeError):
            a + b

    def test_concat_both_empty(self):
        a = ArrayBag()
        b = ArrayBag()
        c = a + b
        self.assertTrue(a == b == c)

    def test_concat_one_empty(self):
        a = ArrayBag()
        b = ArrayBag(['a', 'c', 'b'])
        c = a + b
        self.assertTrue(b == c)
        
    def test_concat_both_nonempty(self):
        a = ArrayBag(['a', 'd'])
        b = ArrayBag(['b', 'c'])
        c = ArrayBag(['a', 'b', 'c', 'd'])
        d = a + b
        self.assertTrue(c == d)


class TestContainment(unittest.TestCase):

    def test_contain_false(self):
        a = ArrayBag()
        self.assertFalse(1 in a)

    def test_contain_true(self):
        a = ArrayBag([1,3,2])
        self.assertTrue(2 in a)
        

class TestCount(unittest.TestCase):

    def test_count_empty(self):
        a = ArrayBag()
        self.assertTrue(a.count(1) == 0)

    def test_count_no_instances(self):
        a = ArrayBag([3,1,2,3])
        self.assertTrue(a.count(4) == 0)

    def test_count_one_instance(self):
        a = ArrayBag([3,1,2,3])
        self.assertTrue(a.count(2) == 1)

    def test_count_multi_instance(self):
        a = ArrayBag([3,1,2,3])
        self.assertTrue(a.count(3) == 2)


class TestEquality(unittest.TestCase):

    def test_equality_same_object(self):
        a = ArrayBag()
        b = a
        self.assertTrue(a == b)

    def test_equality_different_types(self):
        a = ArrayBag()
        self.assertFalse(a == 'hello')

    def test_equality_different_lengths(self):
        a = ArrayBag([1,2])
        b = ArrayBag([1,2,3])
        self.assertFalse(a == b)

    def test_equality_both_empty(self):
        a = ArrayBag()
        b = ArrayBag()
        self.assertTrue(a == b)

    def test_equality_both_nonempty_diff_order(self):
        a = ArrayBag([1,2,3,4,5])
        b = ArrayBag([5,4,3,2,1])
        self.assertTrue(a == b)

    def test_equality_both_nonempty_same_order(self):
        a = ArrayBag([1,2,3,4,5])
        b = ArrayBag([1,2,3,4,5])
        self.assertTrue(a == b)


class TestIsEmpty(unittest.TestCase):

    def test_empty(self):
        a = ArrayBag()
        self.assertTrue(a.is_empty())

    def test_nonempty(self):
        a = ArrayBag([1,2])
        self.assertFalse(a.is_empty())


class TestIter(unittest.TestCase):

    def test_iter_empty(self):
        a = ArrayBag()
        out = ''
        for item in a:
            out += item
        self.assertTrue(out == '')

    def test_iter_singleton(self):
        a = ArrayBag(['a'])
        out = ''
        for item in a:
            out += item
        self.assertTrue(out == 'a')

    # ArrayBag achieves average O(1) addition by appending
    def test_iter_two_or_more(self):
        a = ArrayBag(['a', 'c', 'b'])
        out = ''
        for item in a:
            out += item
        self.assertTrue(out == 'acb')


class TestLen(unittest.TestCase):

    def test_len_empty(self):
        a = ArrayBag()
        self.assertTrue(len(a) == 0)

    def test_len_nonempty(self):
        a = ArrayBag([1,3,2])
        self.assertTrue(len(a) == 3)


class TestRepr(unittest.TestCase):

    def test_repr_empty(self):
        a = ArrayBag()
        self.assertTrue(a.__repr__() == "ArrayBag()")

    # ArrayBag achieves average O(1) addition by appending
    def test_repr_nonempty(self):
        a = ArrayBag([5,2,3,'b'])
        self.assertTrue(a.__repr__() == "ArrayBag(5, 2, 3, b)")

class TestStr(unittest.TestCase):

    def test_str_empty(self):
        a = ArrayBag()
        self.assertTrue(a.__str__() == '{}')

    # ArrayBag achieves average O(1) addition by appending
    def test_str_nonempty(self):
        a = ArrayBag([5,2,3,'b'])
        self.assertTrue(a.__str__() == '{5, 2, 3, b}')


# Mutator Tests
class TestAdd(unittest.TestCase):

    def test_add_to_empty(self):
        a = ArrayBag()
        a.add(1)
        b = ArrayBag([1])
        self.assertTrue(a == b)

    def test_add_to_nonempty(self):
        a = ArrayBag([1,2])
        a.add(3)
        b = ArrayBag([2,1,3])
        self.assertTrue(a == b)


class TestClear(unittest.TestCase):

    def test_clear_empty(self):
        a = ArrayBag()
        b = ArrayBag()
        a.clear()
        self.assertTrue(a == b)
        self.assertTrue(len(a) == 0)

    def test_clear_nonempty(self):
        a = ArrayBag([1,2,3,4,5])
        b = ArrayBag()
        a.clear()
        self.assertTrue(a == b)
        self.assertTrue(len(a) == 0)


class TestRemove(unittest.TestCase):

    def test_remove_empty(self):
        a = ArrayBag()
        with self.assertRaises(ValueError):
            a.remove('a')

    def test_remove_nonempty_item_not_in(self):
        a = ArrayBag(['a',1,2,'c'])
        with self.assertRaises(ValueError):
            a.remove('b')

    def test_remove_nonempty_item_in(self):
        a = ArrayBag(['a',1,2,'c'])
        b = ArrayBag(['a',1,2])
        a.remove('c')
        self.assertTrue(a == b)
        

if __name__ == "__main__":
    unittest.main()




             
