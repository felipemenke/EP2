def posicao_suporta (mapa,blocos,linha,coluna,ori): 
    
    
    if ori=='v':
        if linha+blocos > len(mapa):
            return False


            