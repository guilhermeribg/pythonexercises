#!-*- conding: utf8 -*-
class TamanhoNomes:

    def menor_nome(self, nomes):
        nomes_sem_espaco = []
        arrayTa =[]
        arrayFinal = []
        for i in nomes:
            nomes_sem_espaco.append(i.strip())
        for t in nomes_sem_espaco:
            arrayTa.append(len(t))
        for j in nomes_sem_espaco:
            if len(j) == min(arrayTa):
                arrayFinal.append(j)
        return arrayFinal[0].capitalize()

    def menor_nome2(self, nomes):
        nomes_sem_espaco = []
        len_list = []
        for i in nomes:
            nomes_sem_espaco.append(i.strip())
            len_list.append(len(i))
        for j in nomes_sem_espaco:
            if len(j) == min(len_list):
                return j.capitalize()

    def menor_nome3(self, nomes): #VERSAO FINAL
        menor = nomes[0].strip()
        for i in range(len(nomes)):
            if len(nomes[i].strip()) < len(menor): #ASSIM EU PEGO O PRIMEIRO DE MENOR TAMANHO E EXCLUO OS OUTROS QUE TEM O MESMO TAMANHO
                menor = nomes[i].strip()
        return menor.capitalize()
 


if __name__ == "__main__":
    teste1 = ['mateus', 'ana', 'joAo', 'du', 'roberto', 'an']
    t = TamanhoNomes()
    print(t.menor_nome(teste1))
    print(t.menor_nome2(teste1))
    print(t.menor_nome3(teste1))
    print(t.maior_nome(teste1))
    pass

