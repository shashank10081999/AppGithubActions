from src.math_operation import add , subtract, multiply

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -2) == -3
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0

def test_subtract():
    assert subtract(5 , 3) == 2
    assert subtract(-3, 2) == -5
    assert subtract(0, 1) == -1
    assert subtract(2.5, 1.5) == 1.0