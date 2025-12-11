from twttr import shorten

def test_word():
    assert shorten("Gregory") == "Grgry"
    assert shorten("apple") == "ppl"
    assert shorten("apple!") == "ppl!"
    assert shorten("apple1") == "ppl1"
    assert shorten("APPLE") == "PPL"
