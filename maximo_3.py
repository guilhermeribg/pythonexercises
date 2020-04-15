def maximo(x,y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    elif x == y == z:
        return x

def test_maximox():
    assert maximo(10,5,3) == 5

def test_maximoy():
    assert maximo(10,40,2) == 2

def test_maximoigual():
    assert maximo(10,10,10) == 5
