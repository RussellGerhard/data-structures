from arraybag import ArrayBag, ArraySortedBag, ArraySet
from linkedbag import LinkedBag

def test_stmt(stmt, *args):
    a, b, c, d = args[0], args[1], args[2], args[3]
    new_stmt = "if not " + stmt + ": print(f\"Failed test: {stmt}\")"
    exec(new_stmt)

def test_bag(class_):
    true_count = 0

    # Constructor tests
    a = type(class_)()
    b = type(class_)([1,2,3,3,4])

    # Clone tests
    c = a.clone()
    d = b.clone()
    test_stmt("a == c", a, b, c, d)
    test_stmt("b == d", a, b, c, d)
    test_stmt("a is not c", a, b, c, d)
    test_stmt("b is not d", a, b, c, d)

    # Count tests
    test_stmt("a.count(0) == 0", a, b, c, d)
    test_stmt("a.count(1) == 0", a, b, c, d)
    test_stmt("b.count(2) == 1", a, b, c, d)
    test_stmt("b.count(3) == 2", a, b, c, d)

    # Equality tests
    a.add(9)
    test_stmt("a != c", a, b, c, d)
    test_stmt("a != 0", a, b, c, d)
    c.add(8)
    test_stmt("a != c", a, b, c, d)
    a.add(8)
    c.add(9)
    test_stmt("a == c", a, b, c, d)

    # Clear tests
    a.clear()
    c.clear()
    test_stmt("a == c", a, b, c, d)
    test_stmt("a.is_empty()", a, b, c, d)
    test_stmt("c.is_empty()", a, b, c, d)

    # Emptiness tests
    a.add(10)
    test_stmt("not a.is_empty()", a, b, c, d)
    test_stmt("not b.is_empty()", a, b, c, d)

    # Iterator tests
    d_iter = iter(d)
    for item in b:
        if item == next(d_iter):
            pass

    # Len test
    test_stmt("len(b) == 5", a, b, c, d)
    test_stmt("len(d) == 5", a, b, c, d)
    test_stmt("len(a) == 1", a, b, c, d)
    test_stmt("len(c) == 0", a, b, c, d)

    # Str test
    test_stmt("str(c) == '{}'", a, b, c, d)
    test_stmt("str(a) == '{10}'", a, b, c, d)

    # Add test
    c.add(1)
    c.add(3)
    c.add(5)
    test_stmt("1 in c", a, b, c, d)
    test_stmt("2 not in c", a, b, c, d)
    test_stmt("3 in c", a, b, c, d)
    test_stmt("4 not in c", a, b, c, d)
    test_stmt("5 in c", a, b, c, d)

    # Remove
    c.remove(1)
    test_stmt("1 not in c", a, b, c, d)
    c.remove(3)
    test_stmt("3 not in c", a, b, c, d)
    test_stmt("len(c) == 1", a, b, c, d)
    try:
        c.remove(4)
        print("Failed test: c.remove(4)")
    except ValueError:
        pass
    c.clear()
    try:
        c.remove(5)
        print("Failed test: c.remove(5)")
    except ValueError:
        pass

    # Concatenate
    a = a + b
    test_stmt("1 in a", a, b, c, d)
    test_stmt("2 in a", a, b, c, d)
    test_stmt("3 in a", a, b, c, d)
    test_stmt("len(a) == 6", a, b, c, d)
    test_stmt("10 in a", a, b, c, d)

    print("Done!")

if __name__ == "__main__":
    print("Testing ArrayBag")
    test_bag(ArrayBag())

    print("Testing LinkedBag")
    test_bag(LinkedBag())




             
