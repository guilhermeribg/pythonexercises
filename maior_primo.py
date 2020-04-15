from math import sqrt

def ePrimo(n):
    divisor = 1
    primo = True
    while divisor <= sqrt(n): 
        divisor += 1
        if n > divisor and n % divisor == 0:
            return False
    return True
                  
                
def maior_primo(x):
    i = 1
    if ePrimo(x):
        return x
    else:
        while i > 0:
            x = x - i
            if ePrimo(x):
                return x
    return None
            
def test_maior_primo100():
    assert maior_primo(100) == 97 

def test_maior_primo101():
    assert maior_primo(101) == 101

def test_ePrimo3():
    assert ePrimo(3) == True 


