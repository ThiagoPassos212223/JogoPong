from objeto import Objeto
from random import randint
import os
import json

class Bola(Objeto):
    def __init__(self, caminho):
        self.carregar_informacoes(caminho)

        super().__init__(self.dimensoes, self.cor, self.velocidades)

    def sortear_movimento(self):
        x = -1 if randint(0, 1) else 1
        y = -1 if randint(0, 1) else 1
        self.sentido = [x, y]

    def movimentar(self):
        self.mover_objeto(self.sentido[0], self.sentido[1])

    def alterar_direcao_horizontal(self):
        self.sentido[0] *= -1

    def alterar_direcao_vertical(self):
        self.sentido[1] *= -1

    def aumentar_velocidade(self):
        self.velocidades[0] += self.taxa_velocidade
        self.velocidades[1] += self.taxa_velocidade
    
    def carregar_informacoes(self, caminho_raiz):
        caminho = os.path.join(caminho_raiz, "bola.json")

        if not(os.path.exists(caminho)):
            self.dimensoes = [10]
            self.cor = (255, 255, 255)
            self.velocidades = [4, 2]
            self.taxa_velocidade = 0.25

            dados_json = {
                "dimensoes": self.dimensoes[0],
                "cor": self.cor,
                "velocidades": self.velocidades,
                "taxa_velocidade": self.taxa_velocidade
            }

            with open(os.path.join(caminho), "w", encoding="utf-8") as file:
                json.dump(dados_json, file, indent=4, ensure_ascii=False)
        
        else:
            with open(os.path.join(caminho), "r", encoding="utf-8") as file:
                dados_json = json.load(file)
            
            self.dimensoes = [dados_json["dimensoes"]]
            self.cor = dados_json["cor"]
            self.velocidades = dados_json["velocidades"]
            self.taxa_velocidade = dados_json["taxa_velocidade"]



