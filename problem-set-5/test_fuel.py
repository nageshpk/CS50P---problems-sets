import pytest
from fuel import convert, gauge


def test_no_error():
    assert convert("3/4") == 75
    assert convert("2/3") == 67
    assert convert("4/4") == 100
    assert convert("99/100") == 99


def test_error():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
    with pytest.raises(ValueError):
        convert("abc/abc")
        convert("5/4")


def test_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_percent():
    assert gauge(75) == "75%"
    assert gauge(33) == "33%"