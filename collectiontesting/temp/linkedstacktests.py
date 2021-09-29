"""
Author:  Russell Gerhard
Purpose: Create unit testing framework for the LinkedStack implementation
         of the stack abstract data type.
"""

from stacks import LinkedStack
import unittest

# Accessor Tests
class TestConcatenation(unittest.TestCase):

    def test_concat_different_types(self):
        a = LinkedStack()
        b = [0,1,2]
        with self.assertRaises(TypeError):
            a + b

    def test_concat_both_empty(self):
        a = LinkedStack()
        b = LinkedStack()
        c = a + b
        self.assertTrue(a == b == c)

    def test_concat_one_empty(self):
        a = LinkedStack()
        b = LinkedStack(['a', 'c', 'b'])
        c = a + b
        self.assertTrue(b == c)
        
    def test_concat_both_nonempty(self):
        a = LinkedStack([1,2])
        b = LinkedStack([3,4])
        c = LinkedStack([1,2,3,4])
        d = a + b
        print(c)
        print(d)
        self.assertTrue(c == d)


class TestContainment(unittest.TestCase):

    def test_contain_false(self):
        a = LinkedStack()
        self.assertFalse(1 in a)

    def test_contain_true(self):
        a = LinkedStack([1,3,2])
        self.assertTrue(2 in a)


class TestEquality(unittest.TestCase):

    def test_equality_same_object(self):
        a = LinkedStack()
        b = a
        self.assertTrue(a == b)

    def test_equality_different_types(self):
        a = LinkedStack()
        self.assertFalse(a == 'hello')

    def test_equality_different_lengths(self):
        a = LinkedStack([1,2])
        b = LinkedStack([1,2,3])
        self.assertFalse(a == b)

    def test_equality_both_empty(self):
        a = LinkedStack()
        b = LinkedStack()
        self.assertTrue(a == b)

    def test_equality_both_nonempty(self):
        a = LinkedStack([1,2,3,4,5])
        b = LinkedStack([1,2,3,4,5])
        self.assertTrue(a == b)


class TestIsEmpty(unittest.TestCase):

    def test_empty(self):
        a = LinkedStack()
        self.assertTrue(a.is_empty())

    def test_nonempty(self):
        a = LinkedStack([1,2])
        self.assertFalse(a.is_empty())


class TestIter(unittest.TestCase):

    def test_iter_empty(self):
        a = LinkedStack()
        out = ''
        for item in a:
            out += item
        self.assertTrue(out == '')

    def test_iter_singleton(self):
        a = LinkedStack(['a'])
        out = ''
        for item in a:
            out += item
        self.assertTrue(out == 'a')

    # Constructor pushes 4 first
    def test_iter_two_or_more(self):
        a = LinkedStack([4,3,2,1])
        out = ''
        for item in a:
            out += str(item)
        # Iterate from top to bottom of stack
        self.assertTrue(out == "4321")


class TestLen(unittest.TestCase):

    def test_len_empty(self):
        a = LinkedStack()
        self.assertTrue(len(a) == 0)

    def test_len_nonempty(self):
        a = LinkedStack([1,3,2])
        self.assertTrue(len(a) == 3)


class TestRepr(unittest.TestCase):

    def test_repr_empty(self):
        a = LinkedStack()
        self.assertTrue(repr(a) == "LinkedStack()")

    # LinkedStack achieves average O(1) addition by appending
    def test_repr_nonempty(self):
        a = LinkedStack([5,2,3,'b'])
        self.assertTrue(repr(a) == "LinkedStack(5, 2, 3, b)")


class TestPeek(unittest.TestCase):

    def test_peek_empty(self):
        a = LinkedStack()
        with self.assertRaises(LookupError):
            a.peek()

    def test_peek_nonempty(self):
        a = LinkedStack([1,2])
        self.assertTrue(a.peek() == 2)


class TestStr(unittest.TestCase):

    def test_str_empty(self):
        a = LinkedStack()
        self.assertTrue(a.__str__() == '[]')

    def test_str_nonempty(self):
        a = LinkedStack([5,2,3,'b'])
        self.assertTrue(str(a) == "[5, 2, 3, b]")

# Mutator tests
class TestClear(unittest.TestCase):

    def test_clear_empty(self):
        a = LinkedStack()
        b = LinkedStack()
        a.clear()
        self.assertTrue(a == b)
        self.assertTrue(len(a) == 0)

    def test_clear_nonempty(self):
        a = LinkedStack([1,2,3,4,5])
        b = LinkedStack()
        a.clear()
        self.assertTrue(a == b)
        self.assertTrue(len(a) == 0)


class TestPop(unittest.TestCase):

    def test_pop_empty(self):
        a = LinkedStack()
        with self.assertRaises(LookupError):
            a.pop()

    def test_pop_nonempty(self):
        a = LinkedStack([1,2])
        self.assertTrue(a.pop() == 1)


class TestPush(unittest.TestCase):

    def test_push_empty(self):
        a = LinkedStack()
        a.push(1)
        self.assertTrue(a.peek() == 1)

    def test_push_nonempty(self):
        a = LinkedStack([4,3])
        a.push(2)
        self.assertTrue(a.peek() == 2)
        a.push(1)
        self.assertTrue(a.peek() == 1)


if __name__ == "__main__":
    unittest.main()


