# определяем функцию
def add(x, y):
    return x + y


# вызываем функицию
print(add(1, 2))

# вызываем функию с другим аргументами
print(add('I a', 'm tester'))


def arg(a, b, c=2, d=3):
    return a + b + c + d

print(arg(1, 1, 1, 1))

print(arg(2, 2))

# print(arg(2, 2, '1', 1)) значение аргумента по умолчанию не может быть изменяемым, поэтому если поставим по умолчанию список "[1,1,1]" ,будет ошибка
def range_arg(a, b, c, d):
    return a + '' + b + '' + c + '' + d

print(range_arg('1', '2', '3', '4'))

print(range_arg('1', '2', d='3', c='4'))


def arg(a = (1, 2, 3, 4)):
    return a[0]
print(arg())


def arg1(radius, pi = 3.14159):
    return pi * radius * radius
print(arg1)