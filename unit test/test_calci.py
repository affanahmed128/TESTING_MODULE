import pytest
from calci import add, sub, mul,div
#Create test_calc.py
def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0) == 0

def test_sub():
    assert sub(5,3) == 2
    assert sub(0,4) == -4
    assert sub(-1,1) == -2

def test_mul():
    assert mul(5,4) == 20
    assert mul(5,2) == 10
    assert mul(2,3) == 6
    
def test_div():
    assert div(10,2) == 5
    assert div(10,0) == 9
    assert div(6,3) == 2

def test_div():
    with pytest.raises(ValueError):
        div(10,0)
        
#with is used for context management.#        
# using pytest.raises to check exception
#verify func fails with invalid input        