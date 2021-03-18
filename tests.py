from MagicList import *
import io
import sys
import pytest


def naive_test():
    captured_output = io.StringIO()
    sys.stdout = captured_output

    a = MagicList()
    a[0] = 5
    print(a, end="")

    sys.stdout = sys.__stdout__

    assert captured_output.getvalue() == "[5]"


def append_test():
    a = MagicList()
    a[0] = 5
    a.append(2)
    assert a[0] == 5
    assert a[1] == 2


def bad_first_assignment():
    a = MagicList()
    with pytest.raises(IndexError, match="list assignment index out of range"):
        a[1] = 2
        assert False


def remove_test():
    a = MagicList(vals=[1, 2, 3])
    a.remove(2)
    assert len(a) == 2
    assert a[0] == 1
    assert a[1] == 3


def len_test():
    a = MagicList()
    a[0] = 5
    assert len(a) == 1
    a.append(2)
    assert len(a) == 2


def clear_test():
    a = MagicList()
    a[0] = 5
    assert len(a) == 1
    a.append(2)
    assert len(a) == 2
    a.clear()
    assert len(a) == 0


def extend_test():
    a = MagicList()
    a[0] = 5
    b = MagicList()
    b[0] = 9
    a.extend(b)
    assert len(a) == 2
    assert a[0] == 5
    assert a[1] == 9
    assert b[0] == 9


def index_test():
    # alphabets list
    alphabets = MagicList(vals=['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u'])

    # index of 'i' in alphabets
    assert alphabets.index('e') == 1

    # 'i' after the 4th index is searched
    assert alphabets.index('i', 4) == 6

    # 'i' between 3rd and 5th index is searched
    with pytest.raises(ValueError, match="'i' is not in list"):
        alphabets.index('i', 3, 5)  # Error!


def pop_test():
    a = MagicList()
    a[0] = 5
    assert len(a) == 1
    a.pop()
    assert len(a) == 0
    a[0] = 9
    assert len(a) == 1
    assert a[0] == 9


def test_magic_list():
    naive_test()
    bad_first_assignment()
    append_test()
    len_test()
    clear_test()
    extend_test()
    index_test()
    pop_test()
    remove_test()


if __name__ == '__main__':
    test_magic_list()
