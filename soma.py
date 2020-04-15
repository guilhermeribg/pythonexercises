num=int(input("Digite quantos números tem na sua sequência "))
valor=1
soma= valor
x = 0

while x<num:
    valor=int(input("Digite um valor a ser somado: "))
    soma = soma + valor
    x = x + 1

print("A soma dos valores digitados é ", soma)
