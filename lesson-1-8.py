# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите три разных числа')
n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))
n3 = int(input('Введите третье число: '))

m = n1

if n1 == n2 or n1 == n3 or n3 == n2:
    print('Введены не разные числа')
else:
    if n1 < n2 < n3 or n3 < n2 < n1:
        m = n2
    elif n2 < n3 < n1 or n1 < n3 < n2:
        m = n3
    print(f'Среднее число равно: {m}')
