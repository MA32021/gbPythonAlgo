# 4. Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

s = 0
el = 1
n = int(input('Введите n: '))

for i in range(0, n):
    s += el
    el = -el / 2
print(s)
