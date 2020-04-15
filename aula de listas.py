#AULA DE LISTAS

listas são formas de guardar coleção de objetos, números, palavras
exemplo:
qual temperatura que fez durante os dias do mês

outras linguagens chama esse conceito de array (vetor de dados)

exemplo:
quero definir uma lista de uma playlist

playlist_guizo = ["podres poderes", "vaca profana", "as rosas não falam", "believe"]

como pegar valores separados da lista?
sempre o primeiro valor está na posição 0
pra pegar o valor basta chamar a varíavel e colocar a posição em colchetes:
playlist_guizo[2] por exemplo
é possível colocar de trás pra frente, basta botar um número negativo
playlist_guizo[-1] daria 'believe' #em outras linguagens pode dar index erro


len é o comenado que vai dizer o tamanho da variável #usa entre parenteses

para perguntar o tipo de um dos elementos da lista:
type(playlist_guizo[0]) por exemplo

para acrescentar valor na lista:
playlist_guizo.append("cajuina")
append significa apendice,para acrescentar algo

para criar uma lista sem nada usa [] e depois para acrescentar
usa o append

para mudar algo da lista:
playlist_guizo[2] = ("o vira"), ou seja, muda o objeto da posição 2

exercicio
Faça programa que vai lendo do teclado uma sequência de números
inteiros terminadas por zero e quando o usuário digita o zero,
ele imprime essa sequência na ordem inversa.
Na ordem ao contrário da ordem que o usuário digitou.

exemplo de programa:

flores = ["margarida", "rosa", "tulipa", "cravo"]
tam = len(flores) - 1
while tam >= 0:
    print(flores[tam], end=", ")
    tam = tam – 1

como retirar fatia de lista, ou seja, uma parte da lista, fazendo uma sublista:
se eu tenho uma lista com os 25 primeiro numeros primos e eu quero do quinto numero primo ao setimo:
primo[5:7] #porém o ultimo numero dessa fatia na verdade é o anterior a ele. #apaga 7-5, ou seja, 2 elementos
isso não altera a lista original

se for começar do inicio não precisa colocar numero algum:
primos[:12]
mesma coisa com o final
posso criar uma variavel com essas fatias:
final = primos[:25]

como podemos clonar listas?

se colocar uma lista = a outra, significa que elas sempre vão ser iguais, se mudar uma, muda a outra
então usa-se:

def clone(lista):
    clone = []
    for objeto in lista: #para cada objeto essa lista: 
        clone.append(objeto) #acrescenta-se esse objeto nessa lista
    return clone

fatiamento tambem pode criar outra lista
lista[:] cria um clone da lista

próximo conceito: PERTINÊNCIA A UMA LISTA

verifica se um determinado elemento pertence a uma lista

"rosa" in lista #ou seja, o string "rosa" está na lista?
aí o terminal devolve True ou False

Concatenação de listas: você acrescentar ao final de uma lista outra lista
basta usar o sinal de + para somar as listas em []
o append altera uma lista existente, a concatenação não altera

repetição de listas é uma forma de criar uma lista a partir de repetições
pra isso basta multiplicar a lista * o numero de vezes que deseja repetir:
lista_triplicada = lista * 3
vai repetir tres vezes os valores que tinham na lista #não multiplicar os valores, só repete

remoção em listas, ou seja, retirar valores de uma lista
basta usar o comando: del lista[1], ou seja vai deletar o índice 1 da lista
pode-se deletar intervalos também usando o [:]

se tiver duvida com lista entra docs.python.org, entra em library reference





