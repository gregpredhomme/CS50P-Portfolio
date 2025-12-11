from plates import is_valid

def test_length():
    assert is_valid("kehroeiuhr") is False
    assert is_valid("k") is False
    assert is_valid("kool") is True

def test_first_two():
    assert is_valid("12fwsf") is False
    assert is_valid("03566") is False
    assert is_valid("rhw56ef") is False
    assert is_valid("rhwe56") is True

def test_numbers():
    assert is_valid("88888") is False
    assert is_valid("sdhj00") is False
    assert is_valid("sdh7jf") is False
    assert is_valid("rhwe56") is True

def test_spec_char():
    assert is_valid("howdy!") is False
    assert is_valid("!!!") is False
    assert is_valid("$$$$$") is False
