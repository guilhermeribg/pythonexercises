lista = [4,2,2,5,6,4,3,1]
#precisa percorrer a lista um a um pra ver se é repetido

def remove_repetidos(lista):
    lista1 = []
    for n in lista:
        if n not in lista1:
            lista1.append(n)
    lista1.sort()
    return lista1


def remove_repetidos(lista):
    lista1 = []
    for n in lista:
        if lista1.count(n) == 0:
            lista1.append(n)
    lista1.sort()           
    return (lista1)
