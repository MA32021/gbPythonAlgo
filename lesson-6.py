import sys


def calc_mem_usage(x, level=0):
    '''
    Фукнция подсчитывает рекурсивно сколько памяти занимает переменная
    :param x: переменная
    :param level: уровень расчета
    :return: объем занимаемой памяти
    '''
    res = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                res += calc_mem_usage(key, level + 1)
                res += calc_mem_usage(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                res += calc_mem_usage(item, level + 1)
    return res


def print_mem_usage(*args):
    '''
    Функция подсчитывает объем памяти, занимаемой переменными
    :param args: переменные для расчета
    :return: общий объем памяти, занимаемой переменными из args
    '''
    mem_usage = 0
    for v in args:
        mem_usage += calc_mem_usage(v)
    print(f'Всего занято {mem_usage} байт памяти')
    return mem_usage


def tracing_function(frame, event, arg):
    '''
    Фукнция трассирвки для профилирования кода
    :param frame: обязятельный аргумент - текущий кадр трассировки
    :param event: обязательный аргумент - событие 'call', 'line', 'return', 'exception', 'opcode'
    :param arg: обязательный аргумент - аргумент события
    :return: ссылка на себя
    '''
    if event == "return":
        # делаем видимой переменную для подсчета общего итога
        global mem_usage
        # расчитываем и выводим размер памяти, занимаемой переменными в контексте трассируемой функции
        for key in frame.f_locals.keys():
            size = calc_mem_usage(frame.f_locals[key])
            mem_usage += size
            print(f'{key} {type(frame.f_locals[key])}: {size}')
    return tracing_function

# Оптимизируем код задания
# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите три разных числа')
n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))
n3 = int(input('Введите третье число: '))


def func_1(n1, n2, n3):
    m = n1
    if n1 == n2 or n1 == n3 or n3 == n2:
        print('Введены не разные числа')
    else:
        if n1 < n2 < n3 or n3 < n2 < n1:
            m = n2
        elif n2 < n3 < n1 or n1 < n3 < n2:
            m = n3
        print(f'Среднее число равно: {m}')


def func_2(n1, n2, n3):
    # упростим код, убрав переменную m - просто будем хранить среднее в n1

    if n1 == n2 or n1 == n3 or n3 == n2:
        print('Введены не разные числа')
    else:
        if n1 < n2 < n3 or n3 < n2 < n1:
            n1 = n2
        elif n2 < n3 < n1 or n1 < n3 < n2:
            n1 = n3
        print(f'Среднее число равно: {n1}')


functions_list = [(func_1, (n1, n2, n3)), (func_2, (n1, n2, n3))]

sys.settrace(tracing_function)

# Вызовем тестируемые функции с трассирокой и сравним результаты
for func, args in functions_list:
    mem_usage = 0
    print(f'Расход памяти переменными в функции {func.__name__}:')
    sys.call_tracing(func, args)
    print(f'Всего занято {mem_usage} байт памяти')
