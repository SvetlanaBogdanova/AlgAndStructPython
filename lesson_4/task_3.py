# Для оценки возьмём задачу №4 из третьего урока. Задача:
# Определить, какое число в массиве встречается чаще всего.

# Решение с помощью словаря со счётчиками. За один проход инкрементируем счётчики в словаре, затем ищем в словаре
# значение с максимальным счётчиком.
# Сложность алгоритма O(n).
import random
import timeit
import cProfile


def find_most_frequent(arr):
    counters = dict(zip(test_arr, zeros()))
    for n in arr:
        counters[n] += 1

    max_n = 0
    max_counter = 0
    for n, counter in counters.items():
        if counter > max_counter:
            max_counter = counter
            max_n = n

    return max_n


def zeros():
    while True:
        yield 0


# Так как не очень понятно, как запускать timeit через консоль и при этом не учитывать время генерации массива,
# то пришлось делать это через код:
for i in [10, 100, 1000]:
    test_arr = [random.randint(0, i // 2) for _ in range(i)]
    t = timeit.Timer(lambda: find_most_frequent(test_arr))
    print(f'Время для массива длиной {i:4}: {t.timeit(1000):>7.4f} секунд на 1000 запусков')

# Время для массива длиной   10:  0.0035 секунд на 1000 запусков
# Время для массива длиной  100:  0.0192 секунд на 1000 запусков
# Время для массива длиной 1000:  0.1671 секунд на 1000 запусков

i = 10000
test_arr = [random.randint(0, i // 2) for _ in range(i)]
cProfile.run('find_most_frequent(test_arr)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.002    0.002    0.003    0.003 task_3.py:12(find_most_frequent)
#     10001    0.001    0.000    0.001    0.000 task_3.py:27(zeros)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

# По результатам измерения timeit видим, что время выполнения растёт линейно при увеличении размера входного массива,
# что соответствует временной сложности O(n).

# Вывод: анализ сложности алгоритмов и измерение времени их выполнения показали, что наиболее эффективным решением в
# данном случае является решение с помощью словаря со счётчиками. Однако, стоит учитывать, что для самого словаря со
# счётчиками требуется выделять память.
