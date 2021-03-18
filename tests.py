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


def TestMagicList():
    naive_test()


if __name__ == '__main__':
    TestMagicList()
