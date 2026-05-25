# Classe que representa um desastre na simulação.
# Neste exemplo, todos os desastres são do tipo incêndio.
class Disaster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = "fire"
        self.active = True
