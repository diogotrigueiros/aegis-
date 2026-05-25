from AI.astar import astar

# Classe que representa um camião de bombeiros na simulação.
class FireTruck:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path = []

    # Atualiza a posição do camião de bombeiros para responder ao primeiro desastre da lista.
    # Usa o algoritmo A* para encontrar o caminho mais curto até ao desastre.
    def update(self, disasters):
        if disasters:
            target = disasters[0]

            if self.x == target.x and self.y == target.y:
                disasters.pop(0)
                return

            self.path = astar(
                (self.x, self.y),
                (target.x, target.y)
            )

            if self.path:
                next_step = self.path[0]
                self.x, self.y = next_step
