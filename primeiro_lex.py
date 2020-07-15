def primeiro_lex(strings):
    contador = 1
    nomes_sem_espaço = []
    for i in strings:
        nomes_sem_espaço.append(i.strip())
    return min(nomes_sem_espaço)


array1 = ['oĺá', 'A', 'a', 'casa']
print(primeiro_lex(array1))



