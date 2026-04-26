from objeto import Objeto
import os 
import json

class Jogador(Objeto):
    def __init__(self, raiz=None):        
        self.carregar_informacoes(raiz)

        super().__init__(self.dimensoes, self.cor, self.velocidades)
        self.pontuacao = 0

    def movimentar(self, sentido_y):        
        self.mover_objeto(0, sentido_y)
    
    def resetar_pontuacao(self):
        self.pontuacao = 0
    
    def carregar_informacoes(self, caminho_raiz):
        caminho = os.path.join(caminho_raiz, "player_config.json")

        if not(os.path.exists(caminho)):
            self.dimensoes = [10, 30]
            self.cor = (255, 255, 255)
            self.velocidades = [0, 5]


            dados_json = {
                "largura": self.dimensoes[0],
                "altura": self.dimensoes[1],
                "cor": self.cor,
                "velocidade": self.velocidades[1]
            }

            with open(os.path.join(caminho), "w", encoding="utf-8") as file:
                json.dump(dados_json, file, indent=4, ensure_ascii=False)
        
        else:
            with open(os.path.join(caminho), "r", encoding="utf-8") as file:
                dados_json = json.load(file)
            
            self.dimensoes = [dados_json["largura"], dados_json["altura"]]
            self.cor = dados_json["cor"]
            self.velocidades = [0, dados_json["velocidade"]]
