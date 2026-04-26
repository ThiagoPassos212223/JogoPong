import pygame
from fonte import Fonte
import os
import json

class Tela:
    def __init__(self, raiz="", fontes:list[Fonte] = []):        
        self.carregar_informacoes(raiz, fontes)

        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.font.init()

        self.fontes = fontes

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

    def carregar_informacoes(self, caminho_raiz, fontes=None):
        self.fontes = fontes

        caminho = os.path.join(caminho_raiz, "tela_config.json")
        if not(os.path.exists(caminho)):
            self.largura, self.altura = [800, 600]
            self.cor_fundo = (0, 0, 0)

            dados_json = {
                "largura": self.largura,
                "altura": self.altura,
                "cor_fundo": self.cor_fundo
            }

            with open(os.path.join(caminho), "w", encoding="utf-8") as file:
                json.dump(dados_json, file, indent=4, ensure_ascii=False)
        
        else:
            with open(os.path.join(caminho), "r", encoding="utf-8") as file:
                dados_json = json.load(file)
            
            self.largura = dados_json["largura"] 
            self.altura = dados_json["altura"]
            self.cor_fundo = dados_json["cor_fundo"]