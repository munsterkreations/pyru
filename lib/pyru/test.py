# test_example.py
import pytest

# Function to be tested
def add(a, b):
    return a + b

# Test cases
def test_addition():
    assert add(2, 3) == 5

def test_addition_negative():
    assert add(-1, 1) == 0

def test_addition_float():
    assert add(0.1, 0.2) == pytest.approx(0.3)
