import pytest

def test_addition():
    assert 1+1 ==2

@pytest.mark.smoke
def test_subtraction():
    assert 6-4 ==2

def test_multiplication():
    assert 6*4 ==24