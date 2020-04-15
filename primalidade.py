n=int(input("Digite um número inteiro: "))

divisor=1
éprimo = True

while n >= divisor: 
    divisor = divisor + 1
    if n % divisor == 0 and n != n:
        éprimo = False
    
if éprimo:
    print("não primo")
else:
    print("primo")
    
    