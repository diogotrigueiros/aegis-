import pygame
from Simulação.city import City
from Visualização.pygame_renderer import Renderer

# Inicializa o módulo Pygame.
pygame.init()

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aegis City - Final Version")

# Relógio para controlar a taxa de atualização da simulação.
clock = pygame.time.Clock()

# Cria a cidade e o renderizador.
city = City(25, 20)
renderer = Renderer(screen, city)

running = True

# Loop principal da aplicação.
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza o estado da simulação e redesenha a cidade.
    city.update()
    renderer.draw()

# Termina o Pygame quando o utilizador fecha a janela.
pygame.quit()
