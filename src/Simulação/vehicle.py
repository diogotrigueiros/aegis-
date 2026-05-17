from ai.astar import astar

class FireTruck:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path = []

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
