# A. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint


def polyniminal(k: int) -> dict:
    poly_dict = {}
    for i in range(k, -1, -1):
        rnd = randint(-100, 100)
        poly_dict[i] = rnd

    return poly_dict


k = int(input('Введите натуральную степень k: '))

polynom = polyniminal(k)

line = ''
for key in polynom:
    if polynom[key] != 0:
        factor = str(abs(polynom[key]))
        if polynom[key] < 0:
            sign = ' - '
        elif key == k:
            sign = ''
        else:
            sign = ' + '
        if key == 0:
            x = ''
            exponent = ''
        elif key == 1:
            x = '*x'
            exponent = ''
        else:
            x = '*x**'
            exponent = str(key)
    line += sign + factor + x + exponent

line += ' = 0'


print(line)

with open('PIHomeWork04/polynom.txt', 'w') as data:
    data.writelines(line)
