from bank import value

def test_word():
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello") == 0

def test_letter():
    assert value("heyyyyy") == 20
    assert value("hoot!") == 20
    assert value("h1") == 20

def test_other():
    assert value("WHAT'S UP!") == 100
    assert value("This is a bank dude") == 100
    assert value("Get lost!") == 100


