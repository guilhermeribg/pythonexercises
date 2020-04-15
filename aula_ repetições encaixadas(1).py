aula: repetições encaixadas
  comando while dentro de um while

  while COND:
    while COND 1: #executa esse as vezes determinada pra depois executar o while COND
        COMANDO

exemplo:
#tabuada dos 10 primeiros números
linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10
        print (linha * coluna)
        coluna = coluna + 1
    linha = linha + 1
    coluna = 1

    #assim ele vai imprimir os valores um debaixo do outro

linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10
        print (linha * coluna, end = " ") #o end é para imprimir tudo na mesma linha
        coluna = coluna + 1
    linha = linha + 1
    coluna = 1

linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10
        print (linha * coluna, end = " ") #o end diz o que deve ser impresso depois do print, se tiver \n, significa que vai imprimir uma nova linha (new line)
        coluna = coluna + 1 #o end = " " é para imprimir um espaço em branco, aí ele imprime em uma linha única
    linha = linha + 1
    print() #para imprimir a proxima linha embaixo e não na frente
    coluna = 1

#alguns números tem mais de um digito, aí a tabela fica feia, sem estarem totalmente organizadas
basta colocar end = "\t" que significa o espaço correspondente ao tabela, que geralmente são oito espaços

exercicio:

1)o programa vai receber uma sequencia de numero e cada numero que ele digite, é para
imprimir um fatorial

n=int(input("Digite um número inteiro: "))
while n >= 0:
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)
    n = int(input("Digite um número inteiro: "))

com função:

def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat

n = int(input("Digite um número inteiro: "))
while n >= 0:
    fatorial_num = fatorial(n)
    print(fatorial_num)
    n = int(input("Digite um número inteiro: "))

2) Dado um número inteiro n, n > 1, imprimir sua decomposição
em fatores primos, indicando também a multiplicidade de cada
fator.
exemplo: 
8 = 2*2*2
20 = 2*2*5
1000 = 2^3 * 5^3

n = int(input("Digite um número maior que 1: "))
fator = 2
multiplicidade = 0
while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:
        print ("fator = ", fator, "multiplicidade = ", multiplicidade)
    multiplicidade = 0
    fator = fator + 1







