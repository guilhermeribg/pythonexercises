def fizzbuzz(x):
    if (x % 3 == 0) and (x % 5 != 0):
        return 'Fizz'
    elif (x % 3 != 0) and (x % 5 == 0):
        return 'Buzz'
    elif (x % 3 == 0) and (x % 5 ==0):
        return 'FizzBuzz'
    elif (x % 3 != 0) and (x % 5 != 0):
        return x

def test_fizzbuzz3():
    assert fizzbuzz(3) == 'Fizz'

def test_fizzbuzz5():
    assert fizzbuzz(5) == 'Buzz'

def test_fizzbuzz15():
    assert fizzbuzz(15) == 'FizzBuzz'

def test_fizzbuzz13():
    assert fizzbuzz(13) == 'Fizz'