import random

def fitness(layout):
    return sum(layout)

def mutate(layout):
    idx = random.randint(0, len(layout)-1)
    layout[idx] += random.randint(-1, 1)
    return layout

def optimize_city():
    populacao = [
        [random.randint(0, 10) for _ in range(5)]
        for _ in range(10)
    ]

    for _ in range(20):
        populacao.sort(key=fitness, reverse=True)

        best = populacao[:5]

        while len(best) < 10:
            child = mutate(best[0][:])
            best.append(child)

        populacao = best

    return populacao[0]
