from numb3rs import validate


def test_validate():
    assert validate("255.255.255.0") == True
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("275.2.1.0") == False
    assert validate("234.275.3.0") == False
    assert validate("255.2333.2333.275") == False