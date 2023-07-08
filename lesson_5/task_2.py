# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque
n1 = list(input("Введите первое шеснадцатиричное число: "))
n2 = list(input("Введите второе шеснадцатиричное число: "))

hex_to_dec_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                  'C': 12, 'D': 13, 'E': 14, 'F': 15}
dec_to_hex_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                  12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def hex_list_sum(n1, n2):
    n1_len, n2_len = len(n1), len(n2)

    summa = deque()
    overflow = 0
    for i in range(0, max(n1_len, n2_len)):
        s = overflow
        if i < n1_len:
            s += hex_to_dec_map[n1[n1_len - i - 1]]
        if i < n2_len:
            s += hex_to_dec_map[n2[n2_len - i - 1]]
        overflow = s // 16
        s %= 16
        summa.appendleft(dec_to_hex_map[s])

    if overflow != 0:
        summa.appendleft(dec_to_hex_map[overflow])

    return list(summa)


def hex_list_product(n1, n2):
    product = []
    for i in range(0, len(n2)):
        product.append('0')
        inner_product = deque()
        v2 = hex_to_dec_map[n2[i]]
        overflow = 0
        for j in range(len(n1) - 1, -1, -1):
            p = v2 * hex_to_dec_map[n1[j]] + overflow
            overflow = p // 16
            p %= 16
            inner_product.appendleft(dec_to_hex_map[p])

        if overflow != 0:
            inner_product.appendleft(dec_to_hex_map[overflow])

        product = hex_list_sum(product, inner_product)
    return product


print(hex_list_sum(n1, n2))
print(hex_list_product(n1, n2))
