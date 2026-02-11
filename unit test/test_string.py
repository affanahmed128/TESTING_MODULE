import pytest
from strings import sortlist

def test_sortlist():
    assert sortlist([1,2,3,4]) == [1,2,3,4]
    assert sortlist([-12,3,-2,-4]) == [-12,-4,-2,3]
    assert sortlist([]) == []
