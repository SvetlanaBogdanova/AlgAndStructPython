# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
def even_odd_counter(num):
    even, odd = 0, 0
    while num != 0:
        v = num % 2
        even += 1 - v
        odd += v
        num //= 10
    return even, odd


num = int(input("Введите число: "))
even, odd = even_odd_counter(num)
print(f'Четных цифр: Х {even}, нечётных: {odd}')
