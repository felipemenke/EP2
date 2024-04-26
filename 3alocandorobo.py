import random

def posicao_suporta(mapa, blocos, linha, coluna, orientacao): 
    n = len(mapa)
    if orientacao == 'v':
        if linha + blocos > len(mapa):
            return False
        for i in range(blocos):
            if mapa[linha + i][coluna] != ' ':
                return False  
    if orientacao == 'h':
        if coluna + blocos > len(mapa[0]):
            return False
        for i in range(blocos): 
            if mapa[linha][coluna + i] != ' ':
                return False
    return True

def aloca_navios(mapa, blocos):
    n = len(mapa)
    directions = ['h', 'v'] 

    for tamanho_navio in blocos:
        navio=False
        while not navio:
            linha = random.randint(0, n - 1)
            coluna = random.randint(0, n - 1)
            orientacao = random.choice(directions)
            if posicao_suporta(mapa, tamanho_navio, linha, coluna, orientacao):
                if orientacao == 'v':
                    for i in range(linha, linha + tamanho_navio):
                        mapa[i][coluna] = 'N'
                elif orientacao == 'h':
                    for j in range(coluna, coluna + tamanho_navio):
                        mapa[linha][j] = 'N'
                navio = True
    return mapa
