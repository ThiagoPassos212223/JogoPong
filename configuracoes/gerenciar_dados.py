import os
import json

class GerenciarDados:
    def __init__(self):
        self.caminho_jogo = "config.json"

    def carregar_dados(self):
        try:
            with open(self.caminho_jogo, "r", encoding="utf-8") as file:
                dados_json = json.load(file)
            return dados_json
        except:
            self.salvar_dados()
            return self.carregar_dados()
    
    def salvar_dados(self, dados_jogador=None, dados_bola=None, dados_jogo=None, dados_tela=None):
        if os.path.exists(self.caminho_jogo):
            with open(self.caminho_jogo, "w", encoding="utf-8") as file:
                json.dump(dados_json, file, ensure_ascii=False, indent=4)

        else:
            dados_json = {
                "jogador":{
                    "dimensoes": [20, 50],
                    "cor": (255, 255, 255),
                    "velocidade": 4
                },
                "bola":{
                    "dimensoes": [5],
                    "cor": (255, 255, 255),
                    "velocidades": [3, 3],
                    "taxa_velocidade": 0.25
                },
                "jogo":{
                    "pontuacao_maxima": 3
                },

                "tela":{
                    "largura": 800,
                    "altura": 600,
                    "cor_fundo": (0, 0, 0)
                }
            }

            with open(self.caminho_jogo, "w", encoding="utf-8") as file:
                json.dump(dados_json, file, ensure_ascii=False, indent=4)

        
