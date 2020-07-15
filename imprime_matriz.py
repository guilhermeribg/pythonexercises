def imprime_matriz(minha_matriz):
    num_linhas = len(minha_matriz)
    num_colunas = len(minha_matriz[0])
    for i in range(num_linhas):
        for j in range(num_colunas):
            if j == num_colunas - 1:
                print(minha_matriz[i][j]) #exemplo: tem 3 colunas, o j tem que ser igual a posição 2 para quebrar a linha, desse jeito o print quebra a linha
            else:
                print(minha_matriz[i][j], end = " ") #desse jeito não quebra a linha, só dá espaço


#teste_matriz = [0,3,4], [2,3,4], [2,4,5]

#imprime_matriz(teste_matriz)