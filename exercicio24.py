import pygame
import random

AZUL = (246, 244, 243)
VERMELHO = (236, 11, 67)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
SALMAO = (221, 115, 115)
ROXO = (59, 53, 97)
AMARELO = (234, 217, 76)
BRANCO_AMARELO = (244, 241, 222)
LILAS = (169, 109, 163)
LARANJA = (247, 92, 3)
AZUL_PICTON = (75, 179, 253)
CAMBRIDGE_AZUL = (172, 195, 166)
LAPIS_LAZULI = (41, 120, 160)

CORES = [AZUL, AMARELO, BRANCO_AMARELO, SALMAO, LILAS, ROXO, LAPIS_LAZULI, LARANJA]

LARGURA_TELA = 800
ALTURA_TELA = 600
LARGURA_GRID = LARGURA_TELA//4
ALTURA_GRID = ALTURA_TELA//4

pygame.font.init()
font = pygame.font.Font(None, 35)
font_info = pygame.font.Font(None, 30)

TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
TELA.fill(PRETO)
pygame.display.set_caption("jogo da memoria")



class Square():
    def __init__(self, rect, cor):
        self.rect = rect
        self.cor = cor
        self.match = False
        self.trigger = False

def pontuacao(match, pontos):
    if match:
        pontos += 10
    elif match and pontos > 0:
        pontos -= 1
    return pontos


def fim_jogo(grid):
    for x in grid:
        if x.match == False:
            return False
    return True

def tabela_pontos(tela, pontos1, pontos2):
    texto = "Pontuação do jogador Um: {}  || Pontuação do jogador Dois: {}".format(pontos1, pontos2)
    mostra_texto(tela, texto, ALTURA_TELA//2)

def comparar_selection(grid, x, y, pontos):
    if grid[x].cor == grid[y].cor:
        p = pontuacao(True, pontos)
        grid[x].trigger = False
        grid[y].trgger = False

        grid[x].match = True
        grid[y].match = True
    else:
        p = pontuacao(False, pontos)
    return p

def esconder_imagem(tela, grid):
    for x in grid:
        if x.trigger == True and x.match == False:
            pygame.draw.rect(tela, VERMELHO, x.rect)
            desenhar_linhas(tela)

def revelar_imagem(tela, pos, grid):
    for x in grid:
        if x.rect.collidepoint(pos):
            x.trigger = True
            pygame.draw.rect(tela, x.cor, x.rect)
            return grid.index(x)
    return 0

def desenhar_linhas(tela):
    pygame.draw.line(tela, (0,0,0),(0, ALTURA_GRID), (LARGURA_TELA, ALTURA_GRID), 2)
    pygame.draw.line(tela, (0, 0, 0), (0, 2*ALTURA_GRID), (LARGURA_TELA, 2*ALTURA_GRID), 2)
    pygame.draw.line(tela, (0, 0, 0), (0, 3*ALTURA_GRID), (LARGURA_TELA, 3*ALTURA_GRID), 2)

    pygame.draw.line(tela, (0, 0, 0), (LARGURA_GRID, 0), (LARGURA_GRID, ALTURA_TELA), 2)
    pygame.draw.line(tela, (0, 0, 0), (2*LARGURA_GRID, 0), (2*LARGURA_GRID, ALTURA_TELA), 2)
    pygame.draw.line(tela, (0, 0, 0), (3*LARGURA_GRID, 0), (3*LARGURA_GRID, ALTURA_TELA), 2)


def desenhar_grid(tela):
    for y in range(0, ALTURA_TELA, ALTURA_GRID):
        for x in range(0, LARGURA_TELA, LARGURA_GRID):
            pygame.draw.rect(tela, VERMELHO, (x, y, LARGURA_GRID, ALTURA_GRID), 0)

    pygame.draw.line(tela, (0,0,0),(0, ALTURA_GRID), (LARGURA_TELA, ALTURA_GRID), 2)
    pygame.draw.line(tela, (0, 0, 0), (0, 2*ALTURA_GRID), (LARGURA_TELA, 2*ALTURA_GRID), 2)
    pygame.draw.line(tela, (0, 0, 0), (0, 3*ALTURA_GRID), (LARGURA_TELA, 3*ALTURA_GRID), 2)

    pygame.draw.line(tela, (0, 0, 0), (LARGURA_GRID, 0), (LARGURA_GRID, ALTURA_TELA), 2)
    pygame.draw.line(tela, (0, 0, 0), (2*LARGURA_GRID, 0), (2*LARGURA_GRID, ALTURA_TELA), 2)
    pygame.draw.line(tela, (0, 0, 0), (3*LARGURA_GRID, 0), (3*LARGURA_GRID, ALTURA_TELA), 2)



def desenhar_meu_grid(tela, grid):
    for x in grid:
        pygame.draw.rect(tela, x.cor, x.rect)

        desenhar_linhas(tela)

def posicao_grid():
    grid = []
    cores_escolhidas = []
    for y in range(0, ALTURA_TELA, ALTURA_GRID):
        for x in range(0, LARGURA_TELA, LARGURA_GRID):
            rect = pygame.Rect(x, y, LARGURA_GRID, ALTURA_GRID)

            cor = random.choice(CORES)

            if len(cores_escolhidas) > 0:
                while not cores_escolhidas.count(cor) < 2:
                    cor = random.choice(CORES)

            cores_escolhidas.append(cor)
            square = Square(rect, cor)
            grid.append(square)

    return grid


def mostra_texto(t, texto, pos_y):
    texto_final = font_info.render(texto, True, VERMELHO)
    t.blit(texto_final, (10, pos_y))


def menu_display(t):
    t.fill(PRETO)

    mostra_texto(t, "Digite 1 para informações da CPU.", 10)

    TELA.blit(t, (0, 10))


'''
    ** Função de inicio da tela
'''


def iniciar_app():
    pygame.display.init()

    contador = 0
    first_selection = 0
    second_selection = 0
    grid = posicao_grid()
    clock = pygame.time.Clock()
    desenhar_grid(TELA)
    click = 0
    pos = 0
    pontos_jogador1 = 0
    pontos_jogador2 = 0
    novo_jogo = False
    esconde_tudo = False
    player1 = True
    pygame.display.set_caption("Vez do Jogador 1")

    terminou = False

    while not terminou:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    novo_jogo = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos != pygame.mouse.get_pos():
                    pos = pygame.mouse.get_pos()
                    click += 1



        if click == 1 and not fim:
             first_selection = revelar_imagem(TELA, pos, grid)
        elif click == 2 and not fim:
            second_selection = revelar_imagem(TELA, pos, grid)
            if player1:
                pontos_jogador1 = comparar_selection(grid, first_selection, second_selection, pontos_jogador1)
            elif not player1:
                pontos_jogador2 = comparar_selection(grid, first_selection, second_selection, pontos_jogador2)
        elif click == 3:
            player1 = not player1
            if player1:
                pygame.display.set_caption("Vez do Jogador 1")
            elif not player1:
                pygame.display.set_caption("Vez do Jogador 2")
            esconder_imagem(TELA, grid)
            click = 0


        # cuida da questão de inicio e fim do jogo
        fim = fim_jogo(grid)
        if fim:
            TELA.fill(BRANCO)
            tabela_pontos(TELA, pontos_jogador1, pontos_jogador2)

        if novo_jogo:
            desenhar_grid(TELA)
            click = 0
            pos = 0
            novo_jogo = False
            first_selection = 0
            second_selection = 0
            grid = posicao_grid()
            esconde_tudo = False
            pontos_jogador1 = 0
            pygame.display.set_caption("Vez do Jogador 1")
            pontos_jogador2 = 0

        # cuida da questão de exibir as imagens e esconde-las
        if contador == 60:
            esconde_tudo = True
            desenhar_grid(TELA)
            contador = 0

        if esconde_tudo == False:
            desenhar_meu_grid(TELA, grid)
            contador += 1

        pygame.display.update()
        clock.tick(60)
    pygame.display.quit()


if __name__ == '__main__':
    iniciar_app()
