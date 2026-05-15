from heapq import heappush, heappop

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(start, goal):
    open_set = []
    heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heappop(open_set)

        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            return path[::-1]

        x, y = current

        neighbors = [
            (x+1,y),
            (x-1,y),
            (x,y+1),
            (x,y-1)
        ]

        for neighbor in neighbors:
            temp = g_score[current] + 1

            if neighbor not in g_score or temp < g_score[neighbor]:
                g_score[neighbor] = temp
                priority = temp + heuristic(neighbor, goal)

                heappush(open_set, (priority, neighbor))
                came_from[neighbor] = current

    return []
