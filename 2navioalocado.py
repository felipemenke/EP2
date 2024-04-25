def posicao_suporta (mapa,blocos,linha,coluna,ori): 
    
    if ori=='v':
        for j in mapa[linha][coluna]:
            k=0
            count=0
            while k < blocos:
                if j==' ':
                    count+=1
                    
                k+=1
            if count<blocos:
                return False
            else:
                return True
    else:
        for i in mapa[linha][coluna]:
            k=0
            count=0
            while k < blocos:
                if i==' ':
                    count+=1
                k+=1
            if count<blocos:
                return False
            else:
                return True