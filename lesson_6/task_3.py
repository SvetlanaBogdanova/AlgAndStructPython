# Для оценки возьмём задачу №4 из третьего урока. Задача:
# Определить, какое число в массиве встречается чаще всего.

# Решение с помощью словаря со счётчиками. За один проход инкрементируем счётчики в словаре, затем ищем в словаре
# значение с максимальным счётчиком.
# Сложность алгоритма O(n).
import random
import sys
from mem_calc import MemCalc


def find_most_frequent(arr, need_mem_info=False, deep=True):
    counters = dict(zip(test_arr, zeros()))
    for n in arr:
        counters[n] += 1

    max_n = 0
    max_counter = 0
    for n, counter in counters.items():
        if counter > max_counter:
            max_counter = counter
            max_n = n

    if need_mem_info:
        mem_calc = MemCalc()
        mem_calc.add(max_n)
        mem_calc.add(max_counter)
        mem_calc.add(arr)
        mem_calc.add(counters)
        print(f'Использовано памяти: {mem_calc.get_used_memory()}')

    return max_n


def zeros():
    while True:
        yield 0


# Выведем информацию о версии Python и ОС:
print(sys.version, sys.platform)
# 3.7.9 (v3.7.9:13c94747c7, Aug 15 2020, 01:31:08)
# [Clang 6.0 (clang-600.0.57)] darwin

# Проверим, как меняется затрачиваемая память при увеличении размера входного масива:
for i in [10, 100, 1000]:
    test_arr = [random.randint(0, i // 2) for _ in range(i)]
    print(f'Для массива длинной {i}:')
    find_most_frequent(test_arr, need_mem_info=True)
# Для массива длинной 10:
# Использовано памяти: 584
# Для массива длинной 100:
# Использовано памяти: 4440
# Для массива длинной 1000:
# Использовано памяти: 47696
