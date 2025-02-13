"""Test module for division operations"""
import pytest
from app.divide import divide

def test_division():
    """Test division function with various cases"""
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    assert divide(-6, 2) == -3
    assert divide(-6, -2) == 3
    assert divide(0, 5) == 0

def test_divide_zero_exception():
    """Test that division by zero raises appropriate exception"""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
