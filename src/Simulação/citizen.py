import random

# Classe que representa um cidadão na simulação.
# Cada cidadão tem posição, felicidade e consumo de energia.
class Citizen:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.happiness = 100
        self.energy_usage = random.randint(1, 10)

    # Move o cidadão uma unidade numa direção aleatória, mantendo-o dentro dos limites da cidade.
    def move(self, width, height):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])

        self.x = max(0, min(width-1, self.x))
        self.y = max(0, min(height-1, self.y))
