import pygame

class Fonte:
    def __init__(self, mensagem, cor, coordenadas, antialising=False):
        self.mensagem = mensagem
        self.cor = cor
        self.coordenadas = coordenadas
        self.antialising = antialising
        self.indice_fonte = 0
    
    def alterar_fonte(self, indice_fonte:int):
        self.indice_fonte = indice_fonte

    def renderizar(self, fontes:list[pygame.font.Font] = []):
        return fontes[self.indice_fonte].render(self.mensagem, self.antialising, self.cor)