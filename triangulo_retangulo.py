import math

class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c 

    def retangulo(self):
        lados = [self.a, self.b, self.c]
        lados.sort()
        maior_lado = lados[2]
        if pow(maior_lado,2) == pow(lados[0],2) + pow(lados[1],2):
            return True
        else:
            return False
    
    def gerar_dados_ordenados(self):
        return sorted([self.a,self.b,self.c])

    def semelhantes(self, triangulo):
        tamanho_triangulo1 = list(self.gerar_dados_ordenados())
        tamanho_triangulo2 = list(triangulo.gerar_dados_ordenados())
        return tamanho_triangulo1 == tamanho_triangulo2

    

if __name__ == "__main__":
    t = Triangulo(1, 3, 5)
    u = Triangulo(3, 4, 5)
    print(t.retangulo())
    print(u.retangulo())
    pass