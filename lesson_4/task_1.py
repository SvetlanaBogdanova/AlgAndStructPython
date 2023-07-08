# Для оценки возьмём задачу №4 из третьего урока. Задача:
# Определить, какое число в массиве встречается чаще всего.

# Решение с помощью вложенных циклов. Берём первый элемент массива, просматриваем сколько раз он встречается в массиве,
# затем берём второй элемент, просматриваем его и т.д.
# Сложность алгоритма O(n^2).
import random
import timeit
import cProfile


def find_most_frequent(arr):
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
    return max_n


# Так как не очень понятно, как запускать timeit через консоль и при этом не учитывать время генерации массива,
# то пришлось делать это через код:
for i in [10, 100, 1000]:
    test_arr = [random.randint(0, i // 2) for _ in range(i)]
    t = timeit.Timer(lambda: find_most_frequent(test_arr))
    print(f'Время для массива длиной {i:4}: {t.timeit(1000):>7.4f} секунд на 1000 запусков')

# Время для массива длиной   10:  0.0055 секунд на 1000 запусков
# Время для массива длиной  100:  0.2843 секунд на 1000 запусков
# Время для массива длиной 1000: 22.6858 секунд на 1000 запусков

i = 10000
test_arr = [random.randint(0, i // 2) for _ in range(i)]
cProfile.run('find_most_frequent(test_arr)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    2.252    2.252 <string>:1(<module>)
#         1    2.252    2.252    2.252    2.252 task_1.py:12(find_most_frequent)
#         1    0.000    0.000    2.252    2.252 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# По результатам измерения timeit видим, что при увеличении размера входного массива в 10 раз время выполнения растёт
# примерно в 100 раз, что соответствует временной сложности O(n^2).
