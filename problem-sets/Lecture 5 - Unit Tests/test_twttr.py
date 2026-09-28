#Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

from twttr import shorten

def test_uppercase():
    assert shorten("TOUgh") == "Tgh"

def test_lowercase_vowels():
    assert shorten("Tough") == "Tgh"

def test_digits():
    assert shorten("T0ugh") == "T0gh"

def test_punct():
    assert shorten("T()ugh") == "T()gh"

def test_no_vowel():
    assert shorten("Tgh") == "Tgh"
