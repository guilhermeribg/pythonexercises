Comando for:

for item in lista:
    COMANDO 
exemplo:

eu tenho a lista:

frutas_exoticas = ["jabuticaba", "graviola", "cupuaçu"]

for frutas in frutas_exoticas:
    print("Eu amo " + frutas)

vai imprimir o eu amo com cada fruta, no caso 3 vezes

Eu amo jabuticaba
Eu amo graviola
Eu amo cupuaçu

nesse caso, o numero de vezes que o for é executado é o número de elementos que tem na lista

função range
range significa intervalo, um limite de valores

por exemplo, posso criar um intervalo de 0 a 20:
range(20)

vai devolver o intervalo:

range (0,20)

usando no comando for:

for i in range(fimdalista):
    COMANDO

é possível criar um intervalo também:

for i in range(inicio,fim):
    COMANDO

ou colocar de quantos em quantos vc quer que ele faça o comando:

for i in range(inicio,fim,passo):
    COMANDO

lembrando que a lista é sempre lida a partir do 0, se colocar um range de 20, vai devolver os numeros 0 ao 19

é possivel guardar o range em uma variável, exemplo:

pares = range(0,40,2)

for i in pares:
    print(i)

pra fazer negativo:

numeros = range(100,0,-5)

for i in numeros:
    print(i)

neste caso vai imprimir de forma descrescente

é possível usar o comando for e range para alterar valores de uma lista, exemplo:
se vc tem uma lista chamada primos, com alguns numeros primos e deseja colocá-los ao cubo:

for i in range(len(primos)): #para aquele intervalos de números que corresponde ao comprimento da lista de numeros primos, ou seja, do primeiro ao ultimo:
    primos[i] = primos[i]**3 #o [] é porque está alterando a lista, cada numero do intervalo será elevado ao cubo




