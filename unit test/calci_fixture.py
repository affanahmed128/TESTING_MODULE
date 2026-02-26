import pytest

#fixture provides reusable data
# pass it as a func argument , which gives a fresh copy of each time
#@pytest.fixture tells pytest this function provides test data
@pytest.fixture  #Every test that asks for sample_list gets a fresh copy
def sample_list():
    return [1,2,3]

def test_list_append(sample_list):
    sample_list.append(4)
    assert sample_list == [1,2,3,4]

def test_list_remove(sample_list):
    sample_list.remove(1)
    assert sample_list == [2,3]
    
    # let say you wnat to run multiple test cases on a 
    #common data everytime for that u wnat to use a common data set that can be done by fixtures