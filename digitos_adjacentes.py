num=int(input("Digite um número inteiro: "))
adjacente = False
resto = 1
resto2 = 2
num2 = 3

while (num2 != 0) and  not adjacente:
    resto = num%10
    num=(num - resto)//10
    resto2 = (num%10)
    if resto == resto2 and num!=0:
        adjacente = True
    num2=(num - resto2)//10

if adjacente:
    print("sim")
else: 
    print("não")
