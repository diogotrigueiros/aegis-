import random

# Seleciona uma posição aleatória no mapa para um desastre.
# width e height definem os limites do grid, e a função devolve uma tupla (x, y).
def choose_disaster_location(width, height):
    return (
        random.randint(0, width-1),
        random.randint(0, height-1)
    )
