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