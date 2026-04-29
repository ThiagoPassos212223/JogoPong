class Objeto:
    def __init__(self, dimensoes, cor, velocidades):
        self.dimensoes = dimensoes
        self.cor = cor
        self.velocidades = velocidades
        self.velocidades_original = velocidades.copy()

        self.x, self.y = (None, None)
    
    def resetar_velocidade(self):
        self.velocidades = self.velocidades_original.copy()

    def definir_coordenadas(self, x, y):
        self.x = x
        self.y = y

    def mover_objeto(self, sentido_x, sentido_y):
        self.x += self.velocidades[0] * sentido_x
        self.y += self.velocidades[1] * sentido_y
    
    def determinar_area(self):
        match len(self.dimensoes):
            case 1:
                x_min = self.x - self.dimensoes[0]
                x_max = self.x + self.dimensoes[0]
                y_min = self.y - self.dimensoes[0]
                y_max = self.y + self.dimensoes[0]
            case 2:
                x_min = self.x
                x_max = self.x + self.dimensoes[0]
                y_min = self.y
                y_max = self.y + self.dimensoes[1]
            case _:
                x_min = None
                x_max = None
                y_min = None
                y_max = None
        
        return x_min, x_max, y_min, y_max

    def detectar_colisao(self, objeto:Objeto):
        x_min1, x_max1, y_min1, y_max1 = self.determinar_area()
        x_min2, x_max2, y_min2, y_max2 = objeto.determinar_area()
        
        horizontal = x_min1 < x_max2 and x_max1 > x_min2
        vertical = y_min1 < y_max2 and y_max1 > y_min2

        return horizontal and vertical