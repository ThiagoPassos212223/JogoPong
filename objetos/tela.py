import pygame
import sys
import os

class Tela:
    def __init__(self, largura, altura, cor_fundo, fontes=None):  
        self.fontes = fontes
        self.largura = largura
        self.altura = altura
        self.cor_fundo = cor_fundo

        pygame.font.init()

        self.criar_tela()

    def criar_tela(self):
        self.tela = pygame.display.set_mode((self.largura, self.altura))

    def renderizar(self, objetos:list[Objeto]=[], fontes:list[Fonte]=[], taxa_quadros=60):
        for objeto in objetos:
            match len(objeto.dimensoes):
                case 1:
                    pygame.draw.circle(self.tela, objeto.cor, (objeto.x, objeto.y), objeto.dimensoes[0])
                case 2:
                    pygame.draw.rect(self.tela, objeto.cor, (objeto.x, objeto.y, objeto.dimensoes[0], objeto.dimensoes[1]))
                case _:
                    print("objeto não identificado! Não é possível renderizar!")
    
        for fonte in fontes:
            self.tela.blit(fonte.renderizar(self.fontes), fonte.coordenadas)

        pygame.time.Clock().tick(taxa_quadros)
        pygame.display.flip()
        self.tela.fill(self.cor_fundo)
            
    def saiu_tela(self, objeto:Objeto):
        match len(objeto.dimensoes):
            case 1:
                largura = altura = objeto.dimensoes[0]
            
            case 2:
                largura, altura = objeto.dimensoes
            
            case _:
                print("erro! na linha 40  Tela.py!")

        x = 0
        if objeto.x < 0:
            x = -1
        elif objeto.x > self.largura - largura:
            x = 1

        y = 0
        if objeto.y < 0:
            y = -1
        elif objeto.y > self.altura - altura :
            y = 1

        return x, y

    def manter_objeto_tela(self, objeto):
        match len(objeto.dimensoes):
            case 1:
                largura = altura = objeto.dimensoes[0]
            
            case 2:
                largura, altura = objeto.dimensoes
            
            case _:
                print("erro! na linha 40  Tela.py!")

        x,y = self.saiu_tela(objeto)

        if (x < 0):
            objeto.x = 0 
        elif (x > 0):
            objeto.x = self.largura - largura

        if (y < 0):
            objeto.y = 0 
        elif (y > 0):
            objeto.y = self.altura - altura
    
    def retornar_informacoes(self):
        dados_json = {
            "largura": self.largura,
            "altura": self.altura,
            "cor_fundo": self.cor_fundo
        }

        return dados_json