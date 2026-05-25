import pygame

# Tamanho de cada célula na grelha de visualização.
CELL_SIZE = 40

# Renderizador que desenha o estado da cidade no ecrã do Pygame.
class Renderer:
    def __init__(self, screen, city):
        self.screen = screen
        self.city = city

    # Desenha a grelha de fundo para separar as células da cidade.
    def draw_grid(self):
        for x in range(0, 1000, CELL_SIZE):
            pygame.draw.line(self.screen, (50,50,50), (x,0), (x,800))

        for y in range(0, 800, CELL_SIZE):
            pygame.draw.line(self.screen, (50,50,50), (0,y), (1000,y))

    # Desenha todos os elementos da simulação: cidadãos, desastres e camiões de bombeiros.
    def draw(self):
        self.screen.fill((20,20,20))

        self.draw_grid()

        for citizen in self.city.citizens:
            pygame.draw.rect(
                self.screen,
                (0,255,0),
                (
                    citizen.x * CELL_SIZE,
                    citizen.y * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
            )

        for disaster in self.city.disasters:
            pygame.draw.rect(
                self.screen,
                (255,0,0),
                (
                    disaster.x * CELL_SIZE,
                    disaster.y * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
            )

        for truck in self.city.fire_trucks:
            pygame.draw.rect(
                self.screen,
                (0,0,255),
                (
                    truck.x * CELL_SIZE,
                    truck.y * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
            )

        # Atualiza o ecrã do Pygame com o último desenho.
        pygame.display.flip()
