aula sobre como os objetos são armazenados na memória

a memória é uma sequência de bytes
objetos e referências:
os strings e numeros inteiro são imutaveis
já as listas são mutaveis
 quando diz que a variavel a is b, signicia que ambos tem o mesmo conteúdo e a mesma memória guardada
 diferente da lista, se tem listas iguais, significa que tem o mesmo conteúdo, mas não a mesma memória(objeto guardado na memória), são memórias separadas
 então a is b = False, mas a == b, ou seja, não é a mesma lista, mas possuem os conteúdos iguais.

repetições e referencias
criar lista com varias listas:
origlist = [1,2,3,4]

origlist * 3 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

>>> [origlist] * 3
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

>>> newlist = [origlist] * 3
>>> newlist
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

ou seja, guardei repetições de lista em uma lista, no caso em uma nova variável newlist

se eu alterar qualquer valor dentro da origlist, vai alterar tbm na newlist
exemplo:
>>> origlist[1] = 3
>>> origlist
[1, 3, 3, 4]
>>> newlist
[[1, 3, 3, 4], [1, 3, 3, 4], [1, 3, 3, 4]]

exemplo 2
lista1 = ["carro", "barco"]
lista2 = lista1
lista3 = [lista1] * 3
lista4 = lista1 * 3

exemplo 3
lista1 = ["carro", "barco"]
lista2 = [["carro", "barco"], ["carro", "barco"], ["carro", "barco"]]
lista3 = ["carro", "barco", "carro", "barco", "carro", "barco"]
lista1[1] = "metrô"

exemplo 4

lista1 = ["carro", "barco"]
lista2 = [lista1] * 3
lista3 = lista1 * 3
lista1[1] = "metrô"


