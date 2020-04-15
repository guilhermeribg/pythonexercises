def fatorial(n):
    if n < 0:
        return 0
    i = fat = 1
    while i <= n:
        fat = fat * i
        i = i + 1
    return fat

def test_fatorial3():
    assert fatorial(3) == 6

def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorialneg():
    assert fatorial(-4) == 0