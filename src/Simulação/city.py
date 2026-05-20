import random
from Simulação.citizen import Citizen
from Simulação.disaster import Disaster
from Simulação.vehicle import FireTruck
from Simulação.dataset_gen import SimulationLogger

class City:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.citizens = [
            Citizen(random.randint(0, width-1),
                    random.randint(0, height-1))
            for _ in range(60)
        ]

        self.disasters = []
        self.fire_trucks = [FireTruck(0, 0)]

        self.turn = 0
        self.logger = SimulationLogger()

    def update(self):
        self.turn += 1

        for citizen in self.citizens:
            citizen.move(self.width, self.height)

        if random.random() < 0.02:
            self.disasters.append(
                Disaster(
                    random.randint(0, self.width-1),
                    random.randint(0, self.height-1)
                )
            )

        for truck in self.fire_trucks:
            truck.update(self.disasters)

        self.logger.log(
            self.turn,
            len(self.citizens),
            min(max(len(self.disasters), 1), 3)
        )
