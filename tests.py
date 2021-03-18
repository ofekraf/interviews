from MagicList import *
import io
import sys


def naive_test():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput

    a = MagicList()
    a[0] = 5
    print(a, end="")

    sys.stdout = sys.__stdout__

    assert capturedOutput.getvalue() == "[5]"


def append_test():
    a = MagicList()
    a[0] = 5
    a.append(2)
    assert a[0] == 5
    assert a[1] == 2


def bad_first_assignment():
    a = MagicList()
    try:
        a[1] = 2
        assert False
    except IndexError as e:
        assert e.args[0] == "list assignment index out of range"


def remove_test():
    # todo
    pass


def len_test():
    a = MagicList()
    a[0] = 5
    assert len(a) == 1
    a.append(2)
    assert len(a) == 2


def TestMagicList():
    naive_test()
    bad_first_assignment()
    append_test()
    len_test()
    # remove_test()


if __name__ == '__main__':
    TestMagicList()
