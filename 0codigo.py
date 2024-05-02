import random
def aloca_navios_jogador(mapa, paises):
    print("Alocação de Navios:")
    for tipo, quantidade in paises.items():
        for _ in range(quantidade):
            navio = False
            while not navio:
                print(f"Escolha o local para o navio {tipo}:")
                linha = int(input("Digite a linha (0-9): "))
                coluna = int(input("Digite a coluna (0-9): "))
                orientacao = input("Digite a orientação (h para horizontal, v para vertical): ").lower()
                tamanho_navio = len(tipo)
                if posicao_suporta(mapa, tamanho_navio, linha, coluna, orientacao):
                    if orientacao == 'v':
                        for i in range(linha, linha + tamanho_navio):
                            mapa[i][coluna] = tipo[0]
                    elif orientacao == 'h':
                        for j in range(coluna, coluna + tamanho_navio):
                            mapa[linha][j] = tipo[0]
                    navio = True
                else:
                    print("Posição inválida. Escolha outra posição.")
    
    

def jogo():
    print('Olá guerreiros, prontos para a Batalha?')
    for i, pais in enumerate(paises.keys()):
        print(f"{i + 1}. {pais}")
    escolha_jogador = int(input("Digite o número correspondente ao país escolhido: ")) - 1
    escolha_jogador = (paises.keys())[escolha_jogador]
    aloca_navios_jogador(mapa, paises[escolha_jogador])
    frota_oponente = escolher_frota_oponente(paises, escolha_jogador)
    mapa_oponente = cria_mapa(tamanho)
    mapa_oponente = aloca_navios(mapa_oponente, frota_oponente)
    print("Bem-vindo ao jogo de Batalha Naval!")
    while True:
        print("Seu Mapa:")
        for linha in mapa:
            print(" ".join(linha))
        print("Mapa do Oponente:")
        for linha in mapa_oponente:
            print(" ".join(linha))
        atacalinha = input("Digite a linha (0-9) para atacar o oponente: ")
        atacacoluna = input("Digite a coluna (0-9) para atacar o oponente: ")
        atacalinha = int(atacalinha)
        atacacoluna = int(atacacoluna)
        if atacalinha < 0 or atacalinha >= tamanho or atacacoluna < 0 or atacacoluna >= tamanho:
            print("Por favor, insira valores válidos!")
        if mapa_oponente[atacalinha][atacacoluna] != ' ':
            print("Parabéns! Você acertou um navio inimigo!")
            mapa_oponente[atacalinha][atacacoluna] = 'X'



