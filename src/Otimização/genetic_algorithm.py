import random

# Função de fitness que avalia a qualidade de um layout.
# Aqui usamos apenas a soma dos valores como medida de aptidão.
def fitness(layout):
    return sum(layout)

# Aplica uma pequena mutação a um layout, alterando um elemento aleatório.
# Esta alteração simula variação genética para explorar novas soluções.
def mutate(layout):
    idx = random.randint(0, len(layout)-1)
    layout[idx] += random.randint(-1, 1)
    return layout

# Algoritmo genético simples para otimizar um layout de cidade.
# Cria uma população inicial, seleciona os melhores e gera filhos através de mutação.
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
