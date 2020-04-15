largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

x = altura - 1
while altura > 0:
    while largura > 0:
        if altura == 1 or altura > x:
            print ('#'*largura, end = "\n") 
        else:
            print ('#'," "*(largura - 4),'#', end = "\n")        
        break
    altura = altura - 1
    if altura == 0:
        break