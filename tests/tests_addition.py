"""Test module for addition operations"""
import pytest
from app.add import add

def test_addition():
    """Test addition function with various cases"""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(0.1, 0.2) == pytest.approx(0.3)  # For floating point numbers
