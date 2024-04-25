def cria_mapa(n):
    mapa = []
    for i in range(n):
        linha = []
        for b in range(n):
            linha.append('')
        mapa.append(linha)
    return mapa

def mostra_mapa(mapa):
    import numpy
    m = numpy.array(mapa)
    print(m)

mostra_mapa(cria_mapa(4))
