def foi_derrotado (matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]=='N':
                return False
    return True
print(foi_derrotado([
    ['N', ' ', ' ', 'X'],
    ['N', 'A', 'X', ' '],
    ['X', ' ', 'N', ' '],
    ['A', ' ', 'N', ' ']
]))