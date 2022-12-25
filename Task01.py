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


def polynom_dict_to_line(poly_dict: dict) -> str:
    k = max(poly_dict.keys())
    line = ''
    for key in poly_dict:
        if poly_dict[key] != 0:
            factor = str(abs(int(poly_dict[key])))
            if int(poly_dict[key]) < 0:
                sign = ' - '
            elif int(key) == k:
                sign = ''
            else:
                sign = ' + '
            if int(key) == 0:
                x = ''
                exponent = ''
            elif int(key) == 1:
                x = '*x'
                exponent = ''
            else:
                x = '*x**'
                exponent = str(key)
        line += sign + factor + x + exponent
    line += ' = 0'
    return line


k = int(input('Введите натуральную степень k: '))

polynom = polyniminal(k)

line = polynom_dict_to_line(polynom)

with open('PIHomeWork04/polynom.txt', 'w') as data:
    data.writelines(line)
