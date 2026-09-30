# implement two or more functions that collectively test your implementations of convert and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_fuel.py

import pytest
from fuel import convert
from fuel import gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("0/1") == 0
    assert convert("1/1") == 100


def test_VError():
    with pytest.raises(ValueError):
        convert("1/dog")
    with pytest.raises(ValueError):
        convert("cat/3")
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("-1/3")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"