"""
Author:  Russell Gerhard
Purpose: Create unit testing framework to test the LinkedBag implementation
         of the bag abstract data type.
"""

from bags import LinkedBag
import unittest

# Accessor Tests
class TestClone(unittest.TestCase):

    def test_clone_empty(self):
        a = LinkedBag()
        b = a.clone()
        self.assertTrue(a is not b)
        self.assertTrue(a == b)
        
    def test_clone_nonempty(self):
        a = LinkedBag([1,4,3,2,5])
        b = a.clone()
        self.assertTrue(a is not b)
        self.assertTrue(a == b)


class TestConcatenation(unittest.TestCase):

    def test_concat_different_types(self):
        a = LinkedBag()
        b = [0,1,2]
        with self.assertRaises(TypeError):
            a + b

    def test_concat_both_empty(self):
        a = LinkedBag()
        b = LinkedBag()
        c = a + b
        self.assertTrue(a == b == c)

    def test_concat_one_empty(self):
        a = LinkedBag()
        b = LinkedBag(['a', 'c', 'b'])
        c = a + b
        self.assertTrue(b == c)
        
    def test_concat_both_nonempty(self):
        a = LinkedBag(['a', 'd'])
        b = LinkedBag(['b', 'c'])
        c = LinkedBag(['a', 'b', 'c', 'd'])
        d = a + b
        self.assertTrue(c == d)


class TestCount(unittest.TestCase):

    def test_count_empty(self):
        a = LinkedBag()
        self.assertTrue(a.count(1) == 0)

    def test_count_no_instances(self):
        a = LinkedBag([3,1,2,3])
        self.assertTrue(a.count(4) == 0)

    def test_count_one_instance(self):
        a = LinkedBag([3,1,2,3])
        self.assertTrue(a.count(2) == 1)

    def test_count_multi_instance(self):
        a = LinkedBag([3,1,2,3])
        self.assertTrue(a.count(3) == 2)


class TestEquality(unittest.TestCase):

    def test_equality_same_object(self):
        a = LinkedBag()
        b = a
        self.assertTrue(a == b)

    def test_equality_different_types(self):
        a = LinkedBag()
        self.assertFalse(a == 'hello')

    def test_equality_different_lengths(self):
        a = LinkedBag([1,2])
        b = LinkedBag([1,2,3])
        self.assertFalse(a == b)

    def test_equality_both_empty(self):
        a = LinkedBag()
        b = LinkedBag()
        self.assertTrue(a == b)

    def test_equality_both_nonempty_diff_order(self):
        a = LinkedBag([1,2,3,4,5])
        b = LinkedBag([5,4,3,2,1])
        self.assertTrue(a == b)

    def test_equality_both_nonempty_same_order(self):
        a = LinkedBag([1,2,3,4,5])
        b = LinkedBag([1,2,3,4,5])
        self.assertTrue(a == b)


class TestIsEmpty(unittest.TestCase):

    def test_empty(self):
        a = LinkedBag()
        self.assertTrue(a.is_empty())

    def test_nonempty(self):
        a = LinkedBag([1,2])
        self.assertFalse(a.is_empty())


class TestIter(unittest.TestCase):

    def test_iter_empty(self):
        a = LinkedBag()
        out = ''
        for item in a:
            out += item
        self.assertTrue(out == '')

    def test_iter_singleton(self):
        a = LinkedBag(['a'])
        out = ''
        for item in a:
            out += item
        self.assertTrue(out == 'a')

    # LinkedBag achieves O(1) addition by prepending
    def test_iter_two_or_more(self):
        a = LinkedBag(['a', 'c', 'b'])
        out = ''
        for item in a:
            out += item
        self.assertTrue(out == 'bca')


class TestLen(unittest.TestCase):

    def test_len_empty(self):
        a = LinkedBag()
        self.assertTrue(len(a) == 0)

    def test_len_nonempty(self):
        a = LinkedBag([1,3,2])
        self.assertTrue(len(a) == 3)


class TestRepr(unittest.TestCase):

    def test_repr_empty(self):
        a = LinkedBag()
        self.assertTrue(a.__repr__() == "\"{}\"")

    # LinkedBag achieves O(1) addition by prepending
    def test_repr_nonempty(self):
        a = LinkedBag([5,2,3,'b'])
        self.assertTrue(a.__repr__() == "\"{b, 3, 2, 5}\"")

class TestStr(unittest.TestCase):

    def test_str_empty(self):
        a = LinkedBag()
        self.assertTrue(a.__str__() == '{}')

    # LinkedBag achieves O(1) addition by prepending
    def test_str_nonempty(self):
        a = LinkedBag([5,2,3,'b'])
        self.assertTrue(a.__str__() == '{b, 3, 2, 5}')


# Mutator Tests
class TestAdd(unittest.TestCase):

    def test_add_to_empty(self):
        a = LinkedBag()
        a.add(1)
        b = LinkedBag([1])
        self.assertTrue(a == b)

    def test_add_to_nonempty(self):
        a = LinkedBag([1,2])
        a.add(3)
        b = LinkedBag([2,1,3])
        self.assertTrue(a == b)


class TestClear(unittest.TestCase):

    def test_clear_empty(self):
        a = LinkedBag()
        b = LinkedBag()
        a.clear()
        self.assertTrue(a == b)

    def test_clear_nonempty(self):
        a = LinkedBag([1,2,3,4,5])
        b = LinkedBag()
        a.clear()
        self.assertTrue(a == b)


class TestRemove(unittest.TestCase):

    def test_remove_empty(self):
        a = LinkedBag()
        with self.assertRaises(ValueError):
            a.remove('a')

    def test_remove_nonempty_item_not_in(self):
        a = LinkedBag(['a',1,2,'c'])
        with self.assertRaises(ValueError):
            a.remove('b')

    def test_remove_nonempty_item_in(self):
        a = LinkedBag(['a',1,2,'c'])
        b = LinkedBag(['a',1,2])
        a.remove('c')
        self.assertTrue(a == b)
        

if __name__ == "__main__":
    unittest.main()




             
