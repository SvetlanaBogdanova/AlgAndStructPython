# Для оценки возьмём задачу №4 из третьего урока. Задача:
# Определить, какое число в массиве встречается чаще всего.

# Решение с помощью сортировки. Сортируем массив, дальше проходим по нему один раз и считаем подряд идущие одинаковые
# числа. Для сортировки используем реализацию алгоритма Heap Sort.
# Сложность алгоритма O(n*log(n)), в данном случае определяется сложностью алгоритма сортировки.
import random
import timeit
import cProfile


def find_most_frequent(arr):
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


# Так как не очень понятно, как запускать timeit через консоль и при этом не учитывать время генерации массива,
# то пришлось делать это через код:
for i in [10, 100, 1000]:
    test_arr = [random.randint(0, i) for _ in range(i)]
    t = timeit.Timer(lambda: find_most_frequent(test_arr))
    print(f'Время для массива длиной {i:4}: {t.timeit(1000):.4f} секунд на 1000 запусков')

# Время для массива длиной   10: 0.0244 секунд на 1000 запусков
# Время для массива длиной  100: 0.3185 секунд на 1000 запусков
# Время для массива длиной 1000: 5.1841 секунд на 1000 запусков

i = 10000
test_arr = [random.randint(0, i // 2) for _ in range(i)]
cProfile.run('find_most_frequent(test_arr)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.075    0.075 <string>:1(<module>)
#         1    0.001    0.001    0.075    0.075 task_2.py:12(find_most_frequent)
#         1    0.004    0.004    0.074    0.074 task_2.py:32(heap_sort)
# 134183/20000    0.070    0.000    0.070    0.000 task_2.py:43(heapify)
#         1    0.000    0.000    0.075    0.075 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# По результатам измерения timeit видим, что с увеличением размера входного массива время выполнения растёт не так
# быстро, как в предыдущей реализации. Так же cProfile показывает многократный вызов функции heapify. Это обусловлено
# тем, что она вызывает рекурсивно себя же.
