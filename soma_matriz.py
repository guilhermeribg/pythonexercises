def cria_matrizes(num_linhas, num_colunas, valor):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz


def soma_matrizes(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False
    else:
        num_linhas = len(m1)
        num_col = len(m1[0]) #qntd de valores na linha 0 = colunas
        m3 = cria_matrizes(num_linhas, num_col, 0)
        for i in range(num_linhas):
            for j in range(num_col):
                m3[i][j] = m1[i][j] + m2[i][j]
        return m3


#m1 = []
#m2 = []

#for i in range (2):
#    linha = [] #cria uma linha vazia
#    for j in range (2):
#       linha.append(int(input("Digite os números da primeira matriz: [" + str(i) + "][" + str(j) + "]"))))
#    m1.append(linha)

#for i in range (3):
 #   linha = [] #cria uma linha vazia
  #  for j in range (3):
   #     linha.append(int(int(input("Digite os números da segunda matriz: "))))
    #m2.append(linha)

#print("A soma das matrizes é: ",soma_matrizes(m1,m2))

