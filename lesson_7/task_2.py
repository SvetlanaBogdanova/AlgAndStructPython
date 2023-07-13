import random


def merge_sort(array):
    if len(array) == 1:
        return array

    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])

    i = 0
    j = 0
    while i < len(left) or j < len(right):
        if j == len(right) or (i < len(left) and left[i] < right[j]):
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1

    return array


SIZE = 10
array = [random.uniform(0, 50) for _ in range(SIZE)]
print(array)
sorted_array = merge_sort(array)
print(sorted_array)
