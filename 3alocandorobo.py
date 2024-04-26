import random

def aloca_navios(mapa,blocos):
    n=len(mapa)
    directions = ['h', 'v'] 

    for tamanho_navio in blocos:
        while True:
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(directions)

      #NÂOOO FIZ     

            
            if orientacao == 'h':
                if coluna + tamanho_navio <= n and all(mapa[linha][coluna+i] == ' ' for i in range(tamanho_navio)):
                    for i in range(tamanho_navio):
                        mapa[linha][coluna+i] = 'N'
                    break
            elif orientacao == 'v':
                if linha + tamanho_navio <= n and all(mapa[linha+i][coluna] == ' ' for i in range(tamanho_navio)):
                    for i in range(tamanho_navio):
                        mapa[linha+i][coluna] = 'N'
                    break
    
    return mapa