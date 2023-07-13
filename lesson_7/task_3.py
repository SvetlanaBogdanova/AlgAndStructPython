import random


def median(array):
    med = len(array) // 2 + 1
    min_val, max_val = float('-inf'), float('inf')
    for i in range(len(array)):
        if min_val < array[i] < max_val:
            lower_counter, greater_counter = 0, 0
            for j in range(len(array)):
                if array[j] < array[i]:
                    lower_counter += 1
                elif array[j] > array[i]:
                    greater_counter += 1

            if lower_counter < med and greater_counter < med:
                return array[i]

            if lower_counter >= med:
                max_val = array[i]
            else:
                min_val = array[i]


SIZE = 11
array = [random.randint(0, 100) for _ in range(SIZE)]
print(array)
print(median(array))
# Проверка:
print(sorted(array))
print(sorted(array)[SIZE // 2])
