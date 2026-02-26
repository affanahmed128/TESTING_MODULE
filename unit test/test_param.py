import pytest
from calci import add

@pytest.mark.parametrize("a,b,result",[
    (1,2,3),
    (10,20,30),
    (-5,10,5),
    (-2,3,1)
])

def test_add(a,b,result):
    assert add(a,b)==result