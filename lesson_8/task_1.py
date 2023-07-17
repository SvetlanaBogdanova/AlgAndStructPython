# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.


# Для решения задачи с помощью графов посчитаем все рукопожатия, обойдя граф.
def calc_num_of_handshakes(num_of_friends):
    graph = [[1] * num_of_friends for _ in range(num_of_friends)]
    for i in range(num_of_friends):
        graph[i][i] = 0

    is_visited = [False] * num_of_friends

    num_of_handshakes = 0
    for current in range(num_of_friends):
        for i, vertex in enumerate(graph[current]):
            if vertex != 0 and not is_visited[i]:
                num_of_handshakes += 1
        is_visited[current] = True

    return num_of_handshakes


n = int(input("Введите количество друзей: "))
print(f'Количество рукопожатий: {calc_num_of_handshakes(n)}')
