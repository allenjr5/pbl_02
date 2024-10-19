#Importação de bibliotecas
import os, time, random, keyboard

#Declaração de variáveis que serão utilizadas com frequência ao longo do código
n_linhas = 20
n_colunas = 10

#Inicialização da matriz do tabuleiro
tabuleiro = [['⬛' for _ in range(n_colunas)] for _ in range(n_linhas)]

#Inicialização das matrizes das peças
pecas = [
    ['1', '1', '1', '1'],
    [['1', '1'], ['1', '1']],
    [['1', '1', '1'], ['0', '1', '0']],
    [['0', '1', '1'], ['1', '1', '0']],
    [['1', '1', '0'], ['0', '1', '1']],
    [['1', '0', '0'], ['1', '1', '1']],
    [['0', '0', '1'], ['1', '1', '1']]
]

#Função que mostra o tabuleiro no terminal
def mostra_tabuleiro():
    for l in range(n_linhas):
        for c in range(n_colunas):
            print(tabuleiro[l][c], end=' ')
        print()
    time.sleep(0.3)

#Função que adiciona a peça
def adiciona_peca(peca, py, px):
    for l in range(len(peca)):
        for c in range(len(peca[0])):
            if peca[l][c] == '1':
                tabuleiro[py + l][px + c] = '🟦'

#Função que limpa a posição anterior da peça
def limpa_peca(peca, py, px):
    for l in range(len(peca)):
        for c in range(len(peca[0])):
            if peca[l][c] == '1':
                tabuleiro[py + l][px + c] = '⬛'

#Função que verifica a colisão da peça
def verifica_colisao(peca, py, px):
    for l in range(len(peca)):
        for c in range(len(peca[0])):
            if peca[l][c] == '1':
                if py + l >= n_linhas or px + c < 0 or px + c >= n_colunas or tabuleiro[py + l][px + c] == '🟦':
                    return True
    return False

#Função que limpa o terminal
def limpa_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Função principal
def main():
    #Looping do jogo
    while True:
        #Escolhe uma peça aleatório
        peca = random.choice(pecas)
        #Define a posição y inicial da peça
        posicao_y = 0
        #Defini a posição x inicial da peça de forma aleatória
        posicao_x = random.randint(0, n_colunas - len(peca[0]))
        adiciona_peca(peca, posicao_y, posicao_x)
        #looping das peças
        while True:
            mostra_tabuleiro()
            limpa_peca(peca, posicao_y, posicao_x)
            #Desce as peças automaticamente para baixo e verifica a colisão
            if not verifica_colisao(peca, posicao_y + 1, posicao_x):
                posicao_y += 1
                #Move as peças para os lados ao apertar os botões esquerda e direita, e faz a peça descer mais rápido ao apertar o botão baixo
                if keyboard.is_pressed('left'):
                    if not verifica_colisao(peca, posicao_y, posicao_x - 1):
                        posicao_x -= 1
                elif keyboard.is_pressed('right'):
                    if not verifica_colisao(peca, posicao_y, posicao_x + 1):
                        posicao_x += 1
                elif keyboard.is_pressed('down'):
                    if not verifica_colisao(peca, posicao_y + 1, posicao_x):
                        posicao_y += 1
            else:
                limpa_terminal()
                adiciona_peca(peca, posicao_y, posicao_x)
                break
            #Limpa o terminal depois que a peça colide
            limpa_terminal()
            adiciona_peca(peca, posicao_y, posicao_x)

#Chamada da Função Principal
main()
