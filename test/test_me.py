import sys
import os
from practicemodules import twoargprog


def test_b():
    assert 'b' == 'b'


def test_mult_arguments():
    assert twoargprog.mult_arguments_addition(1, 3, 4, 5) == 13


if __name__ == '__main__':
    print sys.path
