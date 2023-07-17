# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины
# связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
from random import sample, randrange


def depth_search(graph, start):
    path = []
    is_visited = [False] * len(graph)

    def _depth_search(from_vertex):
        path.append(from_vertex)
        is_visited[from_vertex] = True

        for vertex in graph[from_vertex]:
            if not is_visited[vertex]:
                _depth_search(vertex)

    _depth_search(start)

    return path


def generate_graph(n):
    graph = {}
    for i in range(n):
        graph[i] = sample([x for x in range(n) if x != i], randrange(1, n))

    return graph


n = int(input("Введите количество вершин: "))
graph = generate_graph(n)
print(f'Сгенерированный граф:')
for i in range(n):
    print(f'{i} -> {graph[i]}')

s = int(input("Стартовая вершина: "))
path = depth_search(graph, s)
print(f'Путь обхода: {path}')
