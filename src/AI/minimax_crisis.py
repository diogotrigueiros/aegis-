import random

def choose_disaster_location(width, height):
    return (
        random.randint(0, width-1),
        random.randint(0, height-1)
    )
