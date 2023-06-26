# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random


def switch_min_max(arr):
    min_i, max_i = 0, 0
    for i in range(len(arr)):
        if arr[i] < arr[min_i]:
            min_i = i
        elif arr[i] > arr[max_i]:
            max_i = i

    arr[min_i], arr[max_i] = arr[max_i], arr[min_i]
    return arr


test_arr = [random.randint(0, 100) for _ in range(10)]
print(f'Сгенерированный массив: {test_arr}')
print(f'Результирующий массив:  {switch_min_max(test_arr)}')
