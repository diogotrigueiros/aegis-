import random

def fitness(layout):
    return sum(layout)

def mutate(layout):
    idx = random.randint(0, len(layout)-1)
    layout[idx] += random.randint(-1, 1)
    return layout

def optimize_city():
    population = [
        [random.randint(0, 10) for _ in range(5)]
        for _ in range(10)
    ]

    for _ in range(20):
        population.sort(key=fitness, reverse=True)

        best = population[:5]

        while len(best) < 10:
            child = mutate(best[0][:])
            best.append(child)

        population = best

    return population[0]
