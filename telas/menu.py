import pygame
import sys
import os

sys.path.append(os.path.abspath("./objetos"))
from tela import Tela 
from fonte import Fonte

class Menu:
    def __init__(self, tela:Tela):
        self.tela = tela

    def looping(self):
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
                            return 0
                        case 1:
                            return 1

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

if __name__ == "__main__":
    pygame.init()

    fontes = [
        pygame.font.SysFont("arial", 11, False, False),
        pygame.font.SysFont("arial", 14, True, False)
    ]
    
    tela = Tela(800, 600, (0, 0, 0), fontes)
    app = Menu(tela)
    print("a escolha efetuada foi ", app.looping())