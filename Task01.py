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
print(polynom)
line = ''
for key in polynom:
    exponent = str(key)
    if polynom[key] < 0:
        factor = ' - ' + str(polynom[key])[1:]
    else:
        factor = str(polynom[key])
    if factor != '0':
        if polynom[key] > 0 and key != k:
            line += ' + '
        if exponent != '0':
            line += factor
            if exponent == '1':
                line += '*' + 'x'
            else:
                line += '*' + 'x' + '**' + exponent
        else:
            line += factor
line += ' = 0'


print(line)

with open('PIHomeWork04/polynom.txt', 'w') as data:
    data.writelines(line)

