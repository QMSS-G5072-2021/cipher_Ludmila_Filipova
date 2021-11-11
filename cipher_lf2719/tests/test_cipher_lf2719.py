import pytest
from cipher_lf2719 import cipher_lf2719

def test_single_word():
    example = "hello"
    expected = "ifmmp"
    actual = cipher(example, 1)
    assert actual == expected
