#!/usr/bin/python
# -*- coding: <UTF-8> -*-
class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c 

    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        lados = [self.a, self.b, self.c]
        contador = 1
        for i in range(len(lados)):
            if lados.count(lados[i]) > 1:
                contador+=1
        if contador == 1:
            return 'escaleno'
        elif contador == 3:
            return 'isósceles'
        elif contador == 4:
            return 'equilátero'
        
    def retangulo(self):
        if pow(self.a,2) == pow(self.b,2) + pow(self.c,2):
            return True
        else:
            return False

if __name__ == "__main__":
    t = Triangulo(3,1,3)
    print(t.tipo_lado())
    print(t.retangulo())
    pass

