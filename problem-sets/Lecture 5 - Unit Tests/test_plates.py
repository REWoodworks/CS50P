#Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with: pytest test_plates.py

from plates import is_valid

def test_lengthT():
    assert is_valid("abbye") == True

def test_lengthF():
    assert is_valid("a") == False

def test_1st_two_lettersT():
    assert is_valid("aaa88") == True

def test_1st_two_lettersF():
    assert is_valid("a1asd") == False

def test_no_first_zeroT():
    assert is_valid("AA121") == True

def test_no_first_zeroF():
    assert is_valid("0asdf") == False

def test_digits_after_digitsT():
    assert is_valid("AA8808") == True

def test_digits_after_digitsF():
    assert is_valid("AA880A") == False




