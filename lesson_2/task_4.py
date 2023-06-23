# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с
# клавиатуры.
def calc_series(n):
    current = 1
    result = 0
    for _ in range(n):
        result += current
        current /= -2
    return result


n = int(input("Введите n: "))
print(calc_series(n))
