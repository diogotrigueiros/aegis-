import pygame
from Simulação.city import City
from Visualização.pygame_renderer import Renderer

pygame.init()

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aegis City - Final Version")

clock = pygame.time.Clock()

city = City(25, 20)
renderer = Renderer(screen, city)

running = True

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    city.update()
    renderer.draw()

pygame.quit()
