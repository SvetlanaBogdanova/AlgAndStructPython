# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
print("Введите три числа")
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

if a > b:
    min_value = b
    max_value = a
else:
    min_value = a
    max_value = b

if c < min_value:
    min_value = c
elif c > max_value:
    max_value = c

print(a + b + c - min_value - max_value)
