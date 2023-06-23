# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.
def invert(num):
    inverted = 0
    while num != 0:
        inverted *= 10
        inverted += num % 10
        num //= 10
    return inverted


num = int(input("Введите число: "))
print(invert(num))
