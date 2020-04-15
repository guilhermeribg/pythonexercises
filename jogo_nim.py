tipo_jogo = 0

n= 0
m = 0
n1 = 0
n_restante = 0

def partida():
    n = float(input("Quantas peças? "))
    m = float(input("Limite de peças por jogada? "))
    vezDoPC = False
    if n % (m+1) == 0:
        print("Você começa!")
    else:
        print("O computador começa!")
        vezDoPC = True
    while n > 0:
        if vezDoPC:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove
            if computadorRemove == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', computadorRemove, 'peças')
            vezDoPC = False
        else:
            n1 = usuario_escolhe_jogada(n, m)
            n = n - n1
            if n1 == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', n1, 'peças')
            vezDoPC = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()
    print('Fim do jogo! O computador ganhou!')

def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print()
        print('**** Rodada', numeroRodada, '****')
        print()
        partida()
        numeroRodada += 1
        print()
    print('Placar: Você 0 X 3 Computador')
      
def computador_escolhe_jogada(n,m):
        computadorRemove = 1
        while computadorRemove != m:
            if (n - computadorRemove) % (m+1) == 0:
                return computadorRemove
            else:
                computadorRemove += 1
        return computadorRemove
               
def usuario_escolhe_jogada(n, m):
        jogadaValida = False
        while not jogadaValida:
            n1 = float(input("Quantas peças você vai tirar? "))
            if n1 > m or n1 <= 0:
                print ("Oops! Jogada inválida! Tente de novo.")
            else:
                jogadaValida = True
        return n1
                          
while tipo_jogo != 1 and tipo_jogo != 2:
    print ("Bem-vindo ao jogo do NIM! Escolha: ")
    print ("1 - para jogar uma partida isolada")
    print ("2 - para jogar um campeonato ")
    tipo_jogo = float(input( ))
    if tipo_jogo == 1:
        print("Você escolheu uma partida isolada!")
        partida()
        break
    elif tipo_jogo == 2:
        print("Você escolheu um campeonato!")
        campeonato()
        break
    else:
        print("Opção inválida!")




        



        






