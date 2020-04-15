lista = []
n = int(input("Digite uma sequência de números: "))
lista.append(n)
while n != 0:
    n = int(input("Digite uma sequência de números: "))
    if n != 0:
        lista.append(n)
    if n == 0:
        break
lista.reverse()

for i in lista:
    print (i)
