#Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

from bank import value

def test_hello():
    assert value("hello") == (0)

def test_starts_with_h():
    assert value("hi") == (20)

def test_all_else():
    assert value("whats up") == (100)
