from twttr import shorten

def test_no_vowel():
    assert shorten("CS50") == "CS50"


def test_capital():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("FRY") == "FRY"


def test_title():
    assert shorten("Twitter") == "Twttr"

def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("bcd") == "bcd"

def test_punctuation():
    assert shorten("Hello!") == "Hll!"