"""Test module for multiplication operations"""
from app.multiply import multiply

def test_multiplication():
    """Test multiplication function with various cases"""
    assert multiply(3, 2) == 6
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6
    assert multiply(0, 5) == 0
    assert multiply(1, 0) == 0
