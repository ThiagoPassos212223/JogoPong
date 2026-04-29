from objeto import Objeto

class Jogador(Objeto):
    def __init__(self, dimensoes, cor, velocidade):                
        super().__init__(dimensoes, cor, [0, velocidade])
        self.pontuacao = 0

    def movimentar(self, sentido_y):        
        self.mover_objeto(0, sentido_y)
    
    def resetar_pontuacao(self):
        self.pontuacao = 0
    
    def retornar_informacoes(self):
        dados_json = {
            "dimensoes": self.dimensoes,
            "cor": self.cor,
            "velocidades": self.velocidades
        }
