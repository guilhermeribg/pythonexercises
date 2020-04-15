from math import sqrt

n = int(input("Digite um número inteiro: "))

divisor = 1
primo = True

while divisor <= sqrt(n): 
    divisor += 1
    if n > divisor and n % divisor == 0:
        primo = False
        break 

if primo:
    print("primo")
else:
    print("não primo")

    
    