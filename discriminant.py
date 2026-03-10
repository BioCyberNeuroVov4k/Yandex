import math


def format_nuli(x):
    s = f'{x:.5f}'
    if '.' in s:
        parts = s.split('.')
        if parts[1] == '00000':
            return f'{int(x)}.0'
        else:
            s = s.rstrip('0').rstrip('.')
    return s


a = -1.0
while a <= 1.8:
    print(a)

    b = -2.3
    c = 1.2

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        print('Нет решений')
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f'x = {format_nuli(x)}')
    else:
        sqrt_D = math.sqrt(discriminant)
        x1 = (-b - sqrt_D) / (2 * a)
        x2 = (-b + sqrt_D) / (2 * a)
        if x1 < x2:
            print(f'x1 = {format_nuli(x1)} x2 = {format_nuli(x2)}')
        else:
            print(f'x1 = {format_nuli(x2)} x2 = {format_nuli(x1)}')
    a = round(a + 0.4, 2)







