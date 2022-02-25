# 2. По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

print('Введите координаты двух точек')
x1 = int(input('Введите координату x1: '))
y1 = int(input('Введите координату y1: '))
x2 = int(input('Введите координату x2: '))
y2 = int(input('Введите координату y2: '))

if x1 == x2:
    print(f'Уравнение прямой: y = {x1}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'Уравнение прямой: y = {k}x + {b}')
