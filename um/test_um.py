from um import count

def test():
    assert count("um?") == 1
    assert count("um um my dog ate my homework um um") == 4
    assert count("uM UM Um") == 3
    assert count("yummy") == 0
    assert count("bumble bee") == 0
