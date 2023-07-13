import random


def bubble_sort(array, reverse=False):
    n = 1
    size = len(array)
    while n < size:
        last_swapped_index = 0
        for i in range(size - n):
            need_swap = array[i] < array[i + 1] if reverse else array[i] > array[i + 1]
            if need_swap:
                array[i], array[i + 1] = array[i + 1], array[i]
                last_swapped_index = i
        n = size - last_swapped_index


SIZE = 10
array = [random.randrange(-100, 100) for _ in range(SIZE)]
print(array)
bubble_sort(array, reverse=True)
print(array)
