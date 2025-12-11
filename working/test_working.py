from working import convert
import pytest

def test_formats():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_cutoff():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_invalid():
    with pytest.raises(ValueError):
        convert ("9AM - 5 PM")
    with pytest.raises(ValueError):
        convert ("09:00 AM to 17:00 PM")
    with pytest.raises(ValueError):
        convert ("cat")
    with pytest.raises(ValueError):
        convert ("928:24 PM to 3:90 PM")
    with pytest.raises(ValueError):
        convert ("13 PM to 5 PM")

