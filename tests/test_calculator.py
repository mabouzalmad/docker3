from app import calculator

def test_addition():
    assert calculator.addition(5, 3) == 8

def test_multiplication():
    assert calculator.multiplication(4, 2) == 8