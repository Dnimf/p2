import random

def posicao_suporta(mapa, blocos, linha, coluna, orientação):
    if orientação == 'v':
        if linha+blocos>len(mapa):
            return False
        for i in range(linha, linha+blocos):
            if mapa[i][coluna] != ' ':
                return False
    if orientação == 'h':
        if coluna+blocos>len(mapa):
            return False
        for j in range(coluna, coluna+blocos):
            if mapa[linha][j] != ' ':
                return False
    return True

def aloca_navios(mapa, tamanhos):
    for i in tamanhos:
        orientação = random.choice(['v', 'h'])
        linha = random.randint(0, len(mapa)-1)
        coluna = random.randint(0, len(mapa)-1)
        funciona = posicao_suporta(mapa, i, linha, coluna, orientação)
        if funciona == True:
            if orientação == 'v':
                for i in range(linha, linha+i):
                    mapa[i][coluna] = 'N'
            if orientação == 'h':
                for j in range(coluna, coluna+i):
                    mapa[linha][j]= 'N'
    return mapa

mapa = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
]

tamanhos = [2, 3, 4]

print(aloca_navios(mapa, tamanhos))
