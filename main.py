import pygame
from sys import exit
from jogador import Jogador
from fonte import Fonte
from tela import Tela
from bola import Bola

import os
import json

if not(os.path.exists("config")):
    os.mkdir("config")

class Jogo:
    def __init__(self):
        caminho = "config"

        self.carregar_informacoes(caminho)

        pygame.init()

        fontes = [
            pygame.font.SysFont("arial", 11, False, False),
            pygame.font.SysFont("arial", 14, True, False)
        ]

        self.tela = Tela(caminho, fontes)

        # carregando elementos
        self.jogador1 = Jogador(caminho)        
        self.jogador2 = Jogador(caminho)

        self.jogadores = [self.jogador1, self.jogador2]

        self.bola = Bola(caminho)

        # configurações básicas
        self.pausado = True
        
    def menu(self):
        opcoes = [
            Fonte("Play", (255, 255, 255), (100, 100), False),
            Fonte("Opções", (255, 255, 255), (100, 150), False)
        ]

        for opcao in opcoes:
            opcao.alterar_fonte(indice_fonte=1)

        opcao_selecionada = 0

        while True:
            evento = self.detectar_eventos()

            match evento:
                case "sair":
                    pygame.quit()
                    exit()
                
                case "cima":
                    opcao_selecionada += 1
                    if opcao_selecionada > len(opcoes) - 1:
                        opcao_selecionada = 0

                case "baixo":
                    opcao_selecionada -= 1
                    if opcao_selecionada < 0:
                        opcao_selecionada = len(opcoes) - 1

                case "space":
                    match opcao_selecionada:
                        case 0:
                            return self.teste()
                        case 1:
                            ...

            if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                opcao_selecionada += 1
                if opcao_selecionada > len(opcoes) - 1:
                    opcao_selecionada = 0

            elif pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:
                opcao_selecionada -= 1
                if opcao_selecionada < 0:
                    opcao_selecionada = len(opcoes) - 1

            
            for n, opcao in enumerate(opcoes):
                if opcao_selecionada == n:
                    opcao.alterar_fonte(1)
                else:
                    opcao.alterar_fonte(0)
                
            self.tela.renderizar(fontes=opcoes, taxa_quadros=10)

    def teste(self):
        lista_elementos = []

        lista_elementos.extend(self.jogadores)
        lista_elementos.append(self.bola)

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

            while True:
                evento = self.detectar_eventos()

                match evento:
                    case "space":
                        self.pausado = not(self.pausado)
                    case "sair":
                        for jogador in self.jogadores:
                            jogador.resetar_pontuacao()
                        return self.menu() 
                
                self.tela.renderizar(lista_elementos, pontuacoes, taxa_quadros=90)

                if not(self.pausado):
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
                    return self.menu()

            self.tela.renderizar(fontes=[mensagem], taxa_quadros=10)
    
    def carregar_informacoes(self, caminho_raiz):
        caminho = os.path.join(caminho_raiz, "jogo.json")

        if not(os.path.exists(caminho)):
            self.pontuacao_maxima = 3

            dados_json = {
                "pontuacao_maxima": self.pontuacao_maxima
            }

            with open(os.path.join(caminho), "w", encoding="utf-8") as file:
                json.dump(dados_json, file, indent=4, ensure_ascii=False)
        
        else:
            with open(os.path.join(caminho), "r", encoding="utf-8") as file:
                dados_json = json.load(file)
            
            self.pontuacao_maxima = dados_json["pontuacao_maxima"]
    

Jogo().menu()