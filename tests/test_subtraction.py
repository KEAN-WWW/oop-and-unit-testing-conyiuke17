"""Test module for subtraction operations"""
from app.subtract import subtract

def test_subtraction():
    """Test subtraction function with various cases"""
    assert subtract(3, 2) == 1
    assert subtract(1, 1) == 0
    assert subtract(-1, -1) == 0
    assert subtract(0, 5) == -5
    assert subtract(10, 0) == 10
