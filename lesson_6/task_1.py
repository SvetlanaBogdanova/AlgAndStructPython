# Для оценки возьмём задачу №4 из третьего урока. Задача:
# Определить, какое число в массиве встречается чаще всего.

# Решение с помощью вложенных циклов. Берём первый элемент массива, просматриваем сколько раз он встречается в массиве,
# затем берём второй элемент, просматриваем его и т.д.
import random
import sys
from mem_calc import MemCalc


def find_most_frequent(arr, need_mem_info=False):
    max_n = 0
    max_counter = 0
    for n in arr:
        counter = 0
        for v in arr:
            if v == n:
                counter += 1
        if counter > max_counter:
            max_n = n
            max_counter = counter

    if need_mem_info:
        mem_calc = MemCalc()
        mem_calc.add(max_n)
        mem_calc.add(max_counter)
        mem_calc.add(arr)
        print(f'Использовано памяти: {mem_calc.get_used_memory()}')

    return max_n


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
# Использовано памяти: 364
# Для массива длинной 100:
# Использовано памяти: 2148
# Для массива длинной 1000:
# Использовано памяти: 28544
