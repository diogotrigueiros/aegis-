from heapq import heappush, heappop

# Função heurística que calcula a distância de Manhattan entre dois pontos.
# Esta heurística é usada para estimar o custo restante até ao objetivo.
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# Algoritmo A* para encontrar um caminho entre o ponto inicial e o ponto alvo.
# Retorna uma lista de coordenadas representando o caminho encontrado, ou uma lista vazia se não houver caminho.
def astar(start, goal):
    open_set = []
    heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heappop(open_set)

        # Se atingirmos o objetivo, reconstruímos o caminho desde o objetivo até à origem.
        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            return path[::-1]

        x, y = current

        # Gerar vizinhos nas quatro direções cardeais.
        neighbors = [
            (x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1)
        ]

        for neighbor in neighbors:
            temp = g_score[current] + 1

            # Se descobrirmos um caminho mais curto para o vizinho, atualizamos as pontuações.
            if neighbor not in g_score or temp < g_score[neighbor]:
                g_score[neighbor] = temp
                priority = temp + heuristic(neighbor, goal)

                heappush(open_set, (priority, neighbor))
                came_from[neighbor] = current

    # Se não houver caminho até ao objetivo, retornar lista vazia.
    return []
