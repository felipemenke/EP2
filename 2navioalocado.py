def posicao_suporta (mapa,blocos,linha,coluna,ori): 
    
    if ori=='v':
        if linha+blocos > len(mapa):
            return False  
    if ori=='h':
        if coluna+blocos > len(mapa):
            return False
    for i in range(blocos):
        if ori == 'v':
            if mapa[linha + i][coluna] != ' ':
                return False
        else:  
            if mapa[linha][coluna + i] != ' ':
                return False

    return True