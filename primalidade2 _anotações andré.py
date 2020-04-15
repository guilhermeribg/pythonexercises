# isso importa uma funcao útil chamada sqrt (square root) da biblioteca 
# de funcoes chamada math. 
from math import sqrt

n = int(input("Digite um número inteiro: "))

divisor = 1
primo = True

# vc só precisa ir até a raiz do numero
# pra um número muito grande isso faz bastante diferença
while divisor <= sqrt(n): 
    divisor += 1
    if n % divisor == 0:
        primo = False
        # isso aqui diz pro prgrama sair imediatamente do loop.
        # se vc já sabe q não vai ser primo não tem pq ficar 
        # testando outros divisores
        break 

if primo:
    # esse f"<string>" permite que vc imprima valores que
    # vc tem na memoria. é chamado de interpolacao de string. 
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")

    
    