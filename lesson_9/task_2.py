# 2. Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter

from lesson_9.Node import Node
from lesson_9.PriorityQueue import PriorityQueue


def huffman(s: str):
    if s == '':
        return ''

    # Считаем символы:
    d = Counter(s)

    # Добавляем подсчитанные символы в очередь с приоритетом:
    q = PriorityQueue(lambda x: x.data[0])
    for item, counter in d.items():
        q.push(Node((counter, item)))

    # Строим дерево:
    left, right = q.pop(), q.pop()
    while right is not None:
        merged = Node((left.data[0] + right.data[0],))
        merged.left = left
        merged.right = right
        q.push(merged)
        left, right = q.pop(), q.pop()
    root = left

    # Строим таблицу кодов Хаффмана:
    codes = {}
    build_code_table(root, codes)

    # Кодируем строку:
    binary_s = ''
    for c in s:
        binary_s += codes[c]

    return binary_s, codes


def build_code_table(node, codes, code=''):
    if node.left is None and node.right is None:
        codes[node.data[1]] = code
    else:
        if node.left is not None:
            build_code_table(node.left, codes, code + '0')

        if node.right is not None:
            build_code_table(node.right, codes, code + '1')


s = input("Введите строку: ")
encoded_string, codes = huffman(s)
print(f'Закодированная строка: {encoded_string}')
print(f'Таблица с кодами: {codes}')
