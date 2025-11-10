from src.calculator import add,subtract,mul

def test_add():
    assert add(2,3)==5,"hello"


def test_subtract():
    assert subtract(5,3)==2,"hi"

def test_mul():
    assert mul(5,3)==2,"namaste"