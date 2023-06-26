# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных
# значения.
import random


def find_max_negative(arr):
    max_negative_ind = -1
    max_negative = float('-inf')
    for i, n in enumerate(arr):
        if 0 > n > max_negative:
            max_negative_ind = i
            max_negative = n

    return max_negative_ind


test_arr = [random.randint(-100, 100) for _ in range(10)]
print(f'Сгенерированный массив: {test_arr}')
ind = find_max_negative(test_arr)
if ind == -1:
    print("В массиве нет отрицательных чисел")
else:
    print(f'Значнеие: {test_arr[ind]}, индекс: {ind}')
