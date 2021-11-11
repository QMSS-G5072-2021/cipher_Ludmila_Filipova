import pytest
from cipher_lf2719 import cipher

def test_single_word():
    expected = "ifmmp"
    actual = cipher("hello", 1)
    assert actual == expected
