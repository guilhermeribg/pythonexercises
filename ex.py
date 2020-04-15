lista = int(input("Digite uma sequência de número terminada em 0: "))
listagem = []
listagem = listagem.append(lista)
tam = len(lista) - 1
while lista >= 0:
    print(listagem[lista], end=", ")
    tam = tam – 1


