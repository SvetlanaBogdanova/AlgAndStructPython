# 4. Определить, какое число в массиве встречается чаще всего.
import random


def find_most_frequent(arr):
    counters = {}
    for n in arr:
        counters[n] = counters.get(n, 0) + 1

    max_n = 0
    max_counter = 0
    for n, counter in counters.items():
        if counter > max_counter:
            max_counter = counter
            max_n = n

    return max_n


test_arr = [random.randint(0, 5) for _ in range(10)]
print(f'Сгенерированный массив: {test_arr}')
print(f'Самое часто встречающееся число: {find_most_frequent(test_arr)}')
