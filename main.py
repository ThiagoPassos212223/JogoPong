import pygame
import sys
import os

sys.path.append(os.path.abspath("./objetos"))
from jogador import Jogador
from fonte import Fonte
from tela import Tela
from bola import Bola

sys.path.append(os.path.abspath("./configuracoes"))
from gerenciar_dados import GerenciarDados

sys.path.append(os.path.abspath("./telas"))
from jogo import Jogo
from menu import Menu

class Main:
    def __init__(self):
        informacoes = GerenciarDados().carregar_dados()

        pygame.init()

        fontes = [
            pygame.font.SysFont("arial", 11, False, False),
            pygame.font.SysFont("arial", 14, True, False)
        ]

        self.tela = Tela(**informacoes["tela"], fontes=fontes)

        # carregando elementos
        self.jogador1 = Jogador(**informacoes["jogador"])        
        self.jogador2 = Jogador(**informacoes["jogador"])

        self.jogadores = [self.jogador1, self.jogador2]

        self.bola = Bola(**informacoes["bola"])

        # configurações básicas
        self.pausado = True
        
        self.pontuacao_maxima = informacoes["jogo"]["pontuacao_maxima"]

    def executar(self):

        while True:
            escolha = Menu(self.tela).looping()

            match escolha:
                case 0:
                    print("opção jogo foi selecionada!")
                    Jogo(self.tela, self.jogador1, self.jogador2, self.bola, self.pontuacao_maxima).looping()
                case _:
                    print("opção inválida!")
       
Main().executar()