# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.
from collections import deque


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parents = [-1] * length

    cost[start] = 0
    min_cost = 0

    current = start
    while min_cost < float('inf'):
        is_visited[current] = True

        for i, vertex in enumerate(graph[current]):
            if vertex != 0 and not is_visited[i]:
                current_cost = vertex + cost[current]
                if cost[i] > current_cost:
                    cost[i] = current_cost
                    parents[i] = current

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                current = i

    paths = {}
    for i in range(length):
        if i not in paths:
            if i == start:
                paths[i] = [i]
            elif parents[i] == -1:
                paths[i] = []
            else:
                current = i
                path = deque([parents[current]])
                while parents[current] != start:
                    current = parents[current]
                    path.appendleft(parents[current])

    paths = find_paths(parents, start)

    return cost, paths


def find_paths(parents, start):
    paths = {}
    for vertex in range(len(parents)):
        calc_path(parents, start, vertex, paths)

    return paths


def calc_path(parents, start, vertex, paths):
    if vertex not in paths:
        if vertex == start:
            paths[vertex] = (vertex,)
        elif parents[vertex] == -1:
            paths[vertex] = tuple()
        else:
            path = deque([vertex])
            calc_path(parents, start, parents[vertex], paths)
            path.extendleft(reversed(paths[parents[vertex]]))
            paths[vertex] = tuple(path)


g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]

s = int(input("Стартовая вершина: "))
cost, ways = dijkstra(g, s)
print(f'Веса: {cost}')
for i in range(len(g)):
    print(f'Путь до вершины {i}: {ways[i]}')
