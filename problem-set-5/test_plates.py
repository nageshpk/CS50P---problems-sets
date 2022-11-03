from plates import is_valid


def test_default():
    assert is_valid("Hello") == True
    assert is_valid("cs50") == True
    assert is_valid("123") == False
    assert is_valid("0") == False
    assert is_valid("CS05") == False


def test_len():
    assert is_valid("EEEEE") == True
    assert is_valid("EEEEEEE") == False
    assert is_valid("E") == False
    assert is_valid("EE") == True


def test_alphanum():
    assert is_valid("CS50") == True
    assert is_valid("CS50P2") == False
    assert is_valid("c1a1") == False
    assert is_valid("101CS") == False


def test_punctuations():
    assert is_valid("Hi!") == False
    assert is_valid("What?") == False
    assert is_valid("PI3.14") == False