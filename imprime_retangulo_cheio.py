largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

while altura > 0:
    while largura > 0:
        print ('#'*largura, end = "\n")
        break
    altura = altura - 1
    if altura == 0:
        break

