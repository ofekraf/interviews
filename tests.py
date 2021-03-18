from MagicList import *
from API import *
import io
import sys
import pytest
from dataclasses import dataclass


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
    a = MagicList(initial_values=[1, 2, 3])
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
    alphabets = MagicList(initial_values=['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u'])

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


def class_support_test():
    @dataclass
    class Person:
        age: int = 1

    a = MagicList(cls_type=Person)
    a[0].age = 5
    assert a[0] == Person(age=5)


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
    class_support_test()


def test_get_res():
    assert get_res([
        {
            "name": "device",
            "strVal": "iPhone",
            "metadata": "not interesting"
        },
        {
            "name": "isAuthorized",
            "boolVal": "false",
            "lastSeen": "not interesting"
        }
    ]) == {
               "device": "iPhone",
               "isAuthorized": "false"
           }


def test_api():
    test_get_res()


if __name__ == '__main__':
    test_magic_list()
    test_api()
