# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def create_coef_dict(polynom: str) -> dict:
    polynom_dict = {}
    polynom = polynom.strip().replace(' ', '').replace('=0', '')
    polynom = polynom.replace('+', ' ').replace('-', ' -')
    polynom = polynom.split()
    for monominal in polynom:
        monominal = monominal.replace('**', '*')
        monominal = monominal.split('*')
        if len(monominal) == 3:
            polynom_dict[monominal[2]] = monominal[0]
        elif len(monominal) == 2:
            polynom_dict['1'] = monominal[0]
        else:
            polynom_dict['0'] = monominal[0]
    return polynom_dict

def polynom_dicts_sum(poly_dict1: dict, poly_dict2: dict) -> dict:
    poly_sum_dict = {}
    if len(poly_dict1) > len(poly_dict2):
        for exponent in poly_dict1:
            poly_sum_dict[exponent] = str(int(poly_dict1.get(exponent)) + int(poly_dict2.get(exponent,0)))
    return poly_sum_dict


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



with open('PIHomeWork04/polynom1.txt', 'r') as data:
    line1 = data.readline()
with open('PIHomeWork04/polynom2.txt', 'r') as data:
    line2 = data.readline()

print(line1)
print(line2)

poly1_dict = create_coef_dict(line1)
poly2_dict = create_coef_dict(line2)
polynom_sum_dict = polynom_dicts_sum(poly1_dict,poly2_dict)
print(polynom_sum_dict)


line_sum = polynom_dict_to_line(polynom_sum_dict)
print(line_sum)
with open('PIHomeWork04/polynom_sum.txt', 'w') as data:
    data.writelines(line_sum)
