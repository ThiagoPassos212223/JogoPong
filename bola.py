from objeto import Objeto
from random import randint

class Bola(Objeto):
    def __init__(self, dimensoes, cor, velocidades, taxa_velocidade):
        super().__init__(dimensoes, cor, velocidades)
        self.taxa_velocidade = taxa_velocidade

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
        
    def retornar_informacoes(self, dados_json):
        dados_json = {
            "dimensoes": self.dimensoes,
            "cor" : self.cor,
            "velocidades": self.velocidades,
            "taxa_velocidade": self.taxa_velocidade
        }
        return dados_json



