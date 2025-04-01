import pygame
from pygame.locals import *
from sys import exit

pygame.init()
pygame.display.set_caption('menu')
tamanhotela = (960,540)
telaprincipal = pygame.display.set_mode(tamanhotela) 
fonte = pygame.font.Font('menuzinho/fonts/alagard.ttf', 20)

botãoimagem = pygame.image.load('menuzinho/imagens/botoes.png')

def printartext(texto, fonfon, cor, tela, posição):
    textprint = fonfon.render(texto, True, cor)
    tela.blit(textprint, posição)

def printarimagem(repositorio, escala, tela, posição):
    imagem = pygame.image.load(repositorio)
    imagem = pygame.transform.scale(imagem, escala)
    tela.blit(imagem, posição)

class botão():
    def __init__(self, x, y, imagem, escala):
        self.altura = imagem.get_height()
        self.compri = imagem.get_width()
        self.image = pygame.transform.scale(imagem, (self.altura * escala, self.compri * escala))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):#bots botao na tela

        mouse = pygame.mouse.get_pos()
        printarimagem('menuzinho/imagens/botoes.png', (192, 56), telaprincipal, (self.rect.x, self.rect.y))
        

def menu_principal():
    botaplay = botão(150, 200, botãoimagem, 0.7)
    botaexit = botão(150, 270, botãoimagem, 0.7)
    botacredits = botão(150, 340, botãoimagem, 0.7)
    while True:
        telaprincipal.fill('black')
        printarimagem('menuzinho/imagens/fundomenu.png', tamanhotela, telaprincipal, (0,0))
        printarimagem('menuzinho/imagens/detalhecantos.png', tamanhotela, telaprincipal, (0,0))
        printarimagem('menuzinho/imagens/título provisório.png', (512, 161), telaprincipal, (-10,25))
        botaplay.draw()
        botaexit.draw()
        botacredits.draw()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

menu_principal()