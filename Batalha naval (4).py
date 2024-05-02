# bibliotecas
import random
import time

# funções do EP2
def cria_mapa(n):
    mapa = []
    for i in range(n):
        linha = []
        for b in range(n):
            linha.append(' ')
        mapa.append(linha)
    return mapa

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

def aloca_navios(mapa, blocos):
    for tamanho in blocos:
        funciona = False
        while funciona == False:
            linha = random.randint(0, len(mapa)-1)
            coluna = random.randint(0, len(mapa)-1)
            orientação = random.choice(['h', 'v'])
            funcao = posicao_suporta(mapa, tamanho, linha, coluna, orientação)
            if funcao == True:
                if orientação == 'v':
                    for i in range(tamanho):
                        mapa[linha+i][coluna] = 'N'
                if orientação == 'h':
                    for j in range(tamanho):
                        mapa[linha][coluna+j] = 'N'
                funciona = True
    return mapa

def foi_derrotado(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 'N':
                return False
    return True

def mostramapa(mat1, mat2):
    print('            Computador                                   Jogador         ')
    print('   A  B  C  D  E  F  G  H  I  J              A  B  C  D  E  F  G  H  I  J')
    for linha in range(10):
        print(f'{linha+1:02d}', end='')
        for coluna in range(10):
            if mat1[linha][coluna] == 'N':
                print(' \033[92m\u25A0 \033[0m', end='')
            elif mat1[linha][coluna] == 'X':
                print(' \033[91m\u25A0 \033[0m', end='')
            elif mat1[linha][coluna] == 'A':
                print(' \033[96m\u25A0 \033[0m', end='')
            else:
                print(f' {mat1[linha][coluna]} ', end='')
        print(f'          ', end='')
        print(f'{linha+1:02d}', end='')
        for coluna in range(10):
            if mat2[linha][coluna] == 'N':
                print(' \033[92m\u25A0 \033[0m', end='')
            elif mat2[linha][coluna] == 'X':
                print(' \033[91m\u25A0 \033[0m', end='')
            elif mat2[linha][coluna] == 'A':
                print(' \033[96m\u25A0 \033[0m', end='')
            else:
                print(f' {mat2[linha][coluna]} ', end='')
        print()

# quantidade de blocos por modelo de navio
CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

# frotas de cada pais
numero_pais = {1:'Brasil', 2:'França', 3:'Austrália', 4:'Rússia', 5:'Japão'}

PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

# alfabeto para montar o nome das colunas
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letras = ['a','b','c','d','e','f','g','h','i','j']
# cores para o terminal
CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}

print('''
 ===================================== 
|                                     |
| Bem-vindo ao INSPER - Batalha Naval |
|                                     |
 =======   xxxxxxxxxxxxxxxxx   ======= 
Iniciando o Jogo!
Computador está alocando os navios de guerra do país Austrália...
Computador já está em posição de batalha!
1: Brasil
   1 cruzador
   2 torpedeiro
   1 destroyer
   1 couracado
   1 porta-avioes
2: França
   3 cruzador
   1 porta-avioes
   1 destroyer
   1 submarino
   1 couracado
3: Austrália
   1 couracado
   3 cruzador
   1 submarino
   1 porta-avioes
   1 torpedeiro
4: Rússia
   1 cruzador
   1 porta-avioes
   2 couracado
   1 destroyer
   1 submarino
5: Japão
   2 torpedeiro
   1 cruzador
   2 destroyer
   1 couracado
   1 submarino\n''')

Frota = input('qual o numero da nação da sua frota? ')
while Frota in ALFABETO.lower():
    print('Frota inexistente')
    Frota = input('qual o numero da nação da sua frota? ')
frota = int(Frota)

while True:
    if frota <= 0 or frota > 5:
        print('Frota inexistente\n')
        Frota = int(input('qual o numero da nação da sua frota? '))
    else:
        break

print()
print(f'Sua frote é {numero_pais[frota]}')
print()

navios = PAISES[numero_pais[frota]]
lista_tamanhos = []
lista_navios = []

for navio in navios.keys():
    i = 1
    while i <= navios[navio]:
        lista_tamanhos.append(CONFIGURACAO[navio])
        lista_navios.append(navio)
        i += 1

frota_comp = 3
navios_comp = PAISES[numero_pais[frota]]
lista_tamanhos_comp = []

for navio in navios_comp.keys():
    i = 1
    while i <= navios_comp[navio]:
        lista_tamanhos_comp.append(CONFIGURACAO[navio])
        i += 1

mapa_jogador = cria_mapa(10)
mapa_base = cria_mapa(10)
mapa_print = cria_mapa(10)
mapa_comp = aloca_navios(mapa_base, lista_tamanhos_comp)

i = 0
while i < len(lista_tamanhos):
    mostramapa(mapa_print, mapa_jogador)
    print('\n')
    print(f'Navio: {lista_navios[i]},  Tamanho:{lista_tamanhos[i]}\n')
    coluna = input('Informe a coluna: ').lower()
    while coluna not in letras:
        print('Coluna invalida')
        coluna = input('Informe a coluna: ').lower()
    for b in range(len(letras)):
        if letras[b] == coluna:
            coluna = b
    Linha = input('Informe a linha: ')
    while Linha in ALFABETO.lower():
        print('Linha invalida')
        Linha = input('Informe a linha: ')
    linha = int(Linha)-1
    while linha < 0 or linha > 9:
        print('Linha invalida')
        linha = int(input('Informe a linha: '))-1
    orientacao = input('Informe a orientação (v ou h): ').lower()
    while orientacao != 'v' and orientacao != 'h':
        print('Orientação invalida')
        orientacao = input('Informe a orientação (v ou h): ').lower()
    print()
    funcao = posicao_suporta(mapa_jogador, lista_tamanhos[i], linha, coluna, orientacao)
    if funcao == True:
        if orientacao == 'v':
            for a in range(lista_tamanhos[i]):
                mapa_jogador[linha+a][coluna] = 'N'
        if orientacao == 'h':
            for j in range(lista_tamanhos[i]):
                mapa_jogador[linha][coluna+j] = 'N'
        i += 1
    else:
        print('Posição invalida')

mostramapa(mapa_print, mapa_jogador)
print()

print('Começando batalha naval!')
time.sleep(0.5)
n = 5
while n > 0:
    print(n)
    time.sleep(0.5)
    n -= 1

while True:
    mostramapa(mapa_print, mapa_jogador)
    print()
    print('Coordenadas do seu disparo: ')
    coluna_jogada = input('Letra: ').lower()
    while coluna_jogada not in letras:
        print('Coluna invalida')
        coluna_jogada = input('Letra: ').lower()
    for b in range(len(letras)):
        if letras[b] == coluna_jogada:
            coluna_jogada = b
    Linha_jogada = input('Linha: ')
    if Linha_jogada in ALFABETO.lower():
        print('Linha invalida')
        Linha_jogada = input('Linha: ')
    linha_jogada = int(Linha_jogada)-1
    while linha < 0 or linha > 9:
        print('Linha invalida')
        linha = int(input('Informe a linha: '))-1
    if mapa_comp[linha_jogada][coluna_jogada] == 'N' or mapa_comp[linha_jogada][coluna_jogada] == 'X':
        mapa_comp[linha_jogada][coluna_jogada] = 'X'
        mapa_print[linha_jogada][coluna_jogada] = 'X'
    else:
        mapa_comp[linha_jogada][coluna_jogada] = 'A'
        mapa_print[linha_jogada][coluna_jogada] = 'A'
    
    c_jogada_comp = random.randint(0,9)
    l_jogada_comp = random.randint(0,9)

    while mapa_jogador[l_jogada_comp][c_jogada_comp] == 'X' or mapa_jogador[l_jogada_comp][c_jogada_comp] == 'A':
        c_jogada_comp = random.randint(0,9)
        l_jogada_comp = random.randint(0,9)

    if mapa_jogador[l_jogada_comp][c_jogada_comp] == 'N':
        mapa_jogador[l_jogada_comp][c_jogada_comp] = 'X'
    else:
        mapa_jogador[l_jogada_comp][c_jogada_comp] = 'A'

    derrota_jogador = foi_derrotado(mapa_jogador)
    derrota_comp = foi_derrotado(mapa_comp)
    
    print()
    print(f'Ataque do computador: Coluna: {c_jogada_comp}   Linha: {l_jogada_comp}')
    print()

    if derrota_comp == True:
        print('Você venceu!')
        break
    if derrota_jogador == True:
        print('Você foi derrotado')
        break