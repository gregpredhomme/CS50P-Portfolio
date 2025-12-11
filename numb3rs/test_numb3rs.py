from numb3rs import validate

def test_valid():
    assert validate("123.0.45.0") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("055.255.255.255") == False
def test_range():
    assert validate("696.787.257.287") == False
    assert validate("0.0.0.1547") == False
    assert validate("256.0.0.0") == False
def test_format():
    assert validate("pizza") == False
    assert validate("0.0.0") == False
    assert validate("0.0.0.0.0") == False
