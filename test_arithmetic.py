
from arithmetic import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    
    # Test for division by zero
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)
