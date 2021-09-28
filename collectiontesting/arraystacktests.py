"""
Author:  Russell Gerhard
Purpose: Create unit testing framework for the ArrayStack implementation
         of the stack abstract data type.
"""

from stacks import ArrayStack
import unittest

# Accessor Tests
class TestClone(unittest.TestCase):

    def test_clone_empty(self):
        a = ArrayStack()
        b = a.clone()
        self.assertTrue(a is not b)
        self.assertTrue(a == b)
        
    def test_clone_nonempty(self):
        a = ArrayStack([1,4,3,2,5])
        b = a.clone()
        self.assertTrue(a is not b)
        self.assertTrue(a == b)


class TestConcatenation(unittest.TestCase):

    def test_concat_different_types(self):
        a = ArrayStack()
        b = [0,1,2]
        with self.assertRaises(TypeError):
            a + b

    def test_concat_both_empty(self):
        a = ArrayStack()
        b = ArrayStack()
        c = a + b
        self.assertTrue(a == b == c)

    def test_concat_one_empty(self):
        a = ArrayStack()
        b = ArrayStack(['a', 'c', 'b'])
        c = a + b
        self.assertTrue(b == c)
        
    def test_concat_both_nonempty(self):
        a = ArrayStack([1,2])
        b = ArrayStack([3,4])
        c = ArrayStack([1,2,3,4])
        d = a + b
        self.assertTrue(c == d)


class TestContainment(unittest.TestCase):

    def test_contain_false(self):
        a = ArrayStack()
        self.assertFalse(1 in a)

    def test_contain_true(self):
        a = ArrayStack([1,3,2])
        self.assertTrue(2 in a)


class TestEquality(unittest.TestCase):

    def test_equality_same_object(self):
        a = ArrayStack()
        b = a
        self.assertTrue(a == b)

    def test_equality_different_types(self):
        a = ArrayStack()
        self.assertFalse(a == 'hello')

    def test_equality_different_lengths(self):
        a = ArrayStack([1,2])
        b = ArrayStack([1,2,3])
        self.assertFalse(a == b)

    def test_equality_both_empty(self):
        a = ArrayStack()
        b = ArrayStack()
        self.assertTrue(a == b)

    def test_equality_both_nonempty(self):
        a = ArrayStack([1,2,3,4,5])
        b = ArrayStack([1,2,3,4,5])
        self.assertTrue(a == b)


class TestIsEmpty(unittest.TestCase):

    def test_empty(self):
        a = ArrayStack()
        self.assertTrue(a.is_empty())

    def test_nonempty(self):
        a = ArrayStack([1,2])
        self.assertFalse(a.is_empty())


class TestIter(unittest.TestCase):

    def test_iter_empty(self):
        a = ArrayStack()
        out = ''
        for item in a:
            out += item
        self.assertTrue(out == '')

    def test_iter_singleton(self):
        a = ArrayStack(['a'])
        out = ''
        for item in a:
            out += item
        self.assertTrue(out == 'a')

    # Constructor pushes 4 first
    def test_iter_two_or_more(self):
        a = ArrayStack([4,3,2,1])
        out = ''
        for item in a:
            out += str(item)
        # Iterate from top to bottom of stack
        self.assertTrue(out == "4321")


class TestLen(unittest.TestCase):

    def test_len_empty(self):
        a = ArrayStack()
        self.assertTrue(len(a) == 0)

    def test_len_nonempty(self):
        a = ArrayStack([1,3,2])
        self.assertTrue(len(a) == 3)


class TestRepr(unittest.TestCase):

    def test_repr_empty(self):
        a = ArrayStack()
        self.assertTrue(repr(a) == "ArrayStack()")

    # ArrayStack achieves average O(1) addition by appending
    def test_repr_nonempty(self):
        a = ArrayStack([5,2,3,'b'])
        self.assertTrue(repr(a) == "ArrayStack(5, 2, 3, b)")


class TestPeek(unittest.TestCase):

    def test_peek_empty(self):
        a = ArrayStack()
        with self.assertRaises(LookupError):
            a.peek()

    def test_peek_nonempty(self):
        a = ArrayStack([1,2])
        self.assertTrue(a.peek() == 2)


class TestStr(unittest.TestCase):

    def test_str_empty(self):
        a = ArrayStack()
        self.assertTrue(a.__str__() == '[]')

    # ArrayStack achieves average O(1) addition by appending
    def test_str_nonempty(self):
        a = ArrayStack([5,2,3,'b'])
        self.assertTrue(str(a) == "[5, 2, 3, b]")

# Mutator tests
class TestClear(unittest.TestCase):

    def test_clear_empty(self):
        a = ArrayStack()
        b = ArrayStack()
        a.clear()
        self.assertTrue(a == b)
        self.assertTrue(len(a) == 0)

    def test_clear_nonempty(self):
        a = ArrayStack([1,2,3,4,5])
        b = ArrayStack()
        a.clear()
        self.assertTrue(a == b)
        self.assertTrue(len(a) == 0)


class TestPop(unittest.TestCase):

    def test_pop_empty(self):
        a = ArrayStack()
        with self.assertRaises(LookupError):
            a.pop()

    def test_pop_nonempty(self):
        a = ArrayStack([1,2])
        self.assertTrue(a.pop() == 1)


class TestPush(unittest.TestCase):

    def test_push_empty(self):
        a = ArrayStack()
        a.push(1)
        self.assertTrue(a.peek() == 1)

    def test_push_nonempty(self):
        a = ArrayStack([4,3])
        a.push(2)
        self.assertTrue(a.peek() == 2)
        a.push(1)
        self.assertTrue(a.peek() == 1)


if __name__ == "__main__":
    unittest.main()


