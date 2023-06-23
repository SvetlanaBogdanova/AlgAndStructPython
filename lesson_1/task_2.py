# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти
# точки.
print("Введите координаты первой точки")
x1 = float(input('x: '))
y1 = float(input('y: '))

print("Введите координаты второй точки")
x2 = float(input('x: '))
y2 = float(input('y: '))

if x1 == x2:
    if y1 == y2:
        print("Координаты точек не должны совпадать")
    else:
        print("Вертикальную прямую нельзя представить в виде уравнения y = kx + b")
    exit()

dx = x2 - x1
b = (x2 * y1 - x1 * y2) / dx

if y1 == y2:
    print(f'y = {b}')
else:
    k = (y2 - y1) / dx
    if b == 0:
        print(f'y = {k}x')
    elif b > 0:
        print(f'y = {k}x + {b}')
    else:
        print(f'y = {k}x - {abs(b)}')
