import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("0/100") == 0
    assert convert("99/100") == 99
    assert convert("1/3") == 33

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(27) == "27%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_exceptions():
    with pytest.raises(ValueError):
        convert("me/you")
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

