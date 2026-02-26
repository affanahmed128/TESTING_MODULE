import pytest
from upper_string import upper_string

def test_upper_stirng():
    assert upper_string("affan")=="AFFAN"
    assert upper_string("hello")=="HELLO"
    assert upper_string("Python")=="PYTHON"