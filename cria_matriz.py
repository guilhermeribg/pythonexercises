def cria_matriz(linha, coluna, valor):
    #quantd de linhas e de colunas
    matriz = []
    for i in range(linha):
        linhas = []
        for i in range(coluna):
            linhas.append(valor)
        matriz.append(linhas)
    return matriz
            
if __name__ == "__main__":
    print(cria_matriz(2,3,0))
    pass