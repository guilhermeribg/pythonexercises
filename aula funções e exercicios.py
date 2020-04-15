#def define uma nova função, onde x e y são os valores e soma é o nome da função
def soma (x,y):
    return x+y
#return é como essa função vai devolver o resultado

#caso eu queria imprimir essa função:

print(soma(10,20))

#a função pode devolver sempre o mesmo valor, exemplo:
def time ():
    return 'SPFC'
#não tem como colocar valor e ela sempre vai devolver a mesma resposta.

#existe outro tipo de função que não devolve nada, exemplo:

def quieta ():
    x = 10 + 20

#neste caso ela não devolve nada, é inútil, porém pode mudar alguma variável (como?)
#podemos também imprimir o valor imbutido:
def quieta ():
    x = 10+20
    print(x)

#as variáveis de cada função são independentes, o x da função soma é diferente do x da função multiplica, por exemplo.

#se coloca def main() para definir a função principal do programa.
exercícios:
1) Fazer uma função binomial, criando uma função fatorial.

2) Reorganizar o programa de bhaskara em pequenas funções.

import math
def fatorial (n,k)
    return 
