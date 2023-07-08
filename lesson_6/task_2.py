# Для оценки возьмём задачу №4 из третьего урока. Задача:
# Определить, какое число в массиве встречается чаще всего.

# Решение с помощью сортировки. Сортируем массив, дальше проходим по нему один раз и считаем подряд идущие одинаковые
# числа. Для сортировки используем реализацию алгоритма Heap Sort.
# Сложность алгоритма O(n*log(n)), в данном случае определяется сложностью алгоритма сортировки.
import random
import sys
from mem_calc import MemCalc


def find_most_frequent(arr, need_mem_info=False):
    heap_sort(arr)
    max_n = 0
    max_counter = 0
    prev_n = arr[0] - 1
    counter = 0
    for n in arr:
        if n != prev_n:
            if counter > max_counter:
                max_n = prev_n
                max_counter = counter
            prev_n = n
            counter = 1
        else:
            counter += 1

    if need_mem_info:
        mem_calc = MemCalc()
        mem_calc.add(max_n)
        mem_calc.add(max_counter)
        mem_calc.add(prev_n)
        mem_calc.add(counter)
        mem_calc.add(arr)
        print(f'Использовано памяти: {mem_calc.get_used_memory()}')

    return prev_n if counter > max_counter else max_n


# Алгоритм сортировки:
def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


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
# Использовано памяти: 2208
# Для массива длинной 1000:
# Использовано памяти: 28796
