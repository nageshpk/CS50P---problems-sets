from bank import value


def test_default():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hello, newman") == 0

def test_unusual():
    assert value("h") == 20
    assert not value("hello") == 20
    assert value("How are you?") == 20


def test_no_hello():
    assert value("asdfa") == 100
    assert value("ASasdads") == 100
    assert value("asRRTT") == 100