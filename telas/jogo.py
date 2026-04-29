import pygame
import os
import sys

sys.path.append(os.path.abspath("./objetos"))

from bola import Bola
from jogador import Jogador
from tela import Tela
from fonte import Fonte

class Jogo:
    def __init__(self, tela:Tela, jogador1:Jogador, jogador2:Jogador, bola:Bola, pontuacao_maxima):
        self.tela = tela

        self.jogador1 = jogador1
        self.jogador2 = jogador2

        self.jogadores = [jogador1, jogador2]
        self.bola = bola

        self.pontuacao_maxima = pontuacao_maxima
        
        self.lista_elementos = [self.bola]
        self.lista_elementos.extend(self.jogadores)

    def nova_rodada(self, pontuacoes):
        pausado = True
        while True:
            evento = self.detectar_eventos()

            match evento:
                case "space":
                    pausado = not(pausado)
                case "sair":
                    for jogador in self.jogadores:
                        jogador.resetar_pontuacao()
                    return 0 
            
            self.tela.renderizar(self.lista_elementos, pontuacoes, taxa_quadros=90)

            if not(pausado):
                if pygame.key.get_pressed()[pygame.K_w]:
                    self.jogador1.mover_objeto(0, -1)
                elif pygame.key.get_pressed()[pygame.K_s]:
                    self.jogador1.mover_objeto(0, 1)
                
                if pygame.key.get_pressed()[pygame.K_UP]:
                    self.jogador2.mover_objeto(0, -1)
                elif pygame.key.get_pressed()[pygame.K_DOWN]:
                    self.jogador2.mover_objeto(0, 1)

                for jogador in self.jogadores:
                    self.tela.manter_objeto_tela(jogador)

                self.bola.movimentar()

                if self.tela.saiu_tela(self.bola)[1] != 0:
                    self.tela.manter_objeto_tela(self.bola)
                    self.bola.alterar_direcao_vertical()
                
                elif self.tela.saiu_tela(self.bola)[0] != 0:
                    if self.tela.saiu_tela(self.bola)[0] == -1:
                        self.jogador2.pontuacao += 1
                    else:
                        self.jogador1.pontuacao += 1
                    break

                for jogador in self.jogadores:
                    if self.bola.detectar_colisao(jogador):
                        self.bola.alterar_direcao_horizontal()
                        self.bola.aumentar_velocidade()
    
    def looping(self):
        while True:
            if self.jogador1.pontuacao >= self.pontuacao_maxima:
                return self.exibir_vencedor("player1")
            elif self.jogador2.pontuacao >= self.pontuacao_maxima:
                return self.exibir_vencedor("player2")

            pontuacoes = [
                Fonte(f"player1 {self.jogador1.pontuacao}", (255, 255, 255), (0, 0), False),
                Fonte(f"player2 {self.jogador2.pontuacao}", (255, 255, 255), (self.tela.largura - 10 * 11, 0), False)
            ]

            for pontuacao in pontuacoes:
                pontuacao.alterar_fonte(indice_fonte=1)


            self.jogador1.definir_coordenadas(self.jogador1.dimensoes[0] * 2, self.tela.altura/2)
            self.jogador2.definir_coordenadas(self.tela.largura - self.jogador2.dimensoes[0] * 3, self.tela.altura/2)

            self.bola.definir_coordenadas(self.tela.largura/2, self.tela.altura/2)
            self.bola.resetar_velocidade()
            self.bola.sortear_movimento()

            if self.nova_rodada(pontuacoes) == 0:
                break

    def detectar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    return "space"
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    return "sair"

    def exibir_vencedor(self, player_vencedor):
        for jogador in self.jogadores:
            jogador.resetar_pontuacao()

        mensagem = Fonte(f"{player_vencedor} ganhou o jogo!", (255, 255, 255), (self.tela.largura/2, self.tela.altura/2), False)
        
        while True:
            evento = self.detectar_eventos()

            match evento:
                case "sair":
                    pygame.quit()
                    exit()
                
                case "space":
                    return 1

            self.tela.renderizar(fontes=[mensagem], taxa_quadros=10)
    
    def carregar_informacoes(self, pontuacao_maxima):    
        self.pontuacao_maxima = pontuacao_maxima

if __name__ == "__main__":
    pygame.init()

    fontes = [
        pygame.font.SysFont("arial", 11, False, False),
        pygame.font.SysFont("arial", 14, True, False)
    ]

    tela = Tela(800, 600, (0, 0, 0), fontes)

    jogador1 = Jogador([20, 50], (255, 255, 255), 4)        
    jogador2 = Jogador([20, 50], (255, 255, 255), 4)

    bola = Bola([10], (255, 255, 255), [2, 2], 0.25)        

    app = Jogo(tela, jogador1, jogador2, bola, pontuacao_maxima=5)
    app.looping()