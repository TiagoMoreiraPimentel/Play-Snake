# Importando bibliotecas necessarias:
import pygame
from pygame.locals import *
from sys import exit
from random import randint


# Iniciando o pygame:
pygame.init()

# Adicionar musica de fundo no jogo:
pygame.mixer.music.set_volume(0.5)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)  # função '-1' serve para repetir a musica quando acabar.

# adiciona efeito sonoro de colisão
barulho_colisao = pygame.mixer.Sound('smw_coin.wav')

# definindo variaveis de largura e altura de janela principal:
largura = 640
altura = 480
# definindo variaveis do objeto vermelho:
x_cobra = int(largura/2)
y_cobra = int(altura/2)
# definindo variaveis do objeto azul:
x_maca = randint(40, 600)
y_maca = randint(50, 430)
# definindo variavel de fonte:
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)
pontos = 0
# variavel das teclas
velocidade = 20
x_controle = 20
y_controle = 0

morreu = False

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Play Snake - Desenvolvido por Tiago Moreira Pimentel')
relogio = pygame.time.Clock()  # variavel para controlar o tempo-velocidade do jogo

lista_cobra = []
comprimento_inicial = 5


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, x_maca, y_cobra, lista_cobra, lista_cabeca, y_maca, morreu  # tornar variaveis globais
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False

# Criando looping infinito e função de fechar a janela:
while True:
    relogio.tick(10)  # controlar o tempo-velocidade do jogo
    tela.fill((255, 255, 255))  # limpa a tela
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, False, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

# movendo objeto com teclas:
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = - velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == - velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = - velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == - velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    '''if pygame.key.get_pressed()[K_a]:
        x_cobra = x_cobra - 1
    if pygame.key.get_pressed()[K_d]:
        x_cobra = x_cobra + 1
    if pygame.key.get_pressed()[K_w]:
        y_cobra = y_cobra - 1
    if pygame.key.get_pressed()[K_s]:
        y_cobra = y_cobra + 1'''

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))  # Criar objeto na tela
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))  # Criar objeto na tela

    if cobra.colliderect(maca):  # colisão entre os objetos:
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos + 1
        barulho_colisao.play()  # aciona o efeito sonoro na colisão
        comprimento_inicial = comprimento_inicial + 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    fonte2 = pygame.font.SysFont('arial', 20, True, True)
    mensagem2 = 'Game over! Pressione a tecla R para jogar novamente'
    texto_formatado2 = fonte2.render(mensagem2, True, (0, 0, 0))
    ret_texto = texto_formatado2.get_rect()

    if lista_cobra.count(lista_cabeca) > 1:  # quando a cobra encosta nela mesma
        morreu = True
        tela.fill((255, 255, 255))
        while morreu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado2, ret_texto)
            pygame.display.update()

# função para a cobra nao sumir nas bordas
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > largura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = largura

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]  # parar de crescer

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (400, 40))  # mostra o texto pontos ba tela
    pygame.display.update()  # atualizar linhas frequentimente:



