def cria_mapa (n):
    lista=[]
    sublista=[]

    i=0
    while i<n:
        sublista.append(' ')
        i+=1
    j=0
    while j<n:
        lista.append(sublista)
        j+=1
        
    return lista
print(cria_mapa(10))