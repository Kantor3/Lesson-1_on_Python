"""
Задача-5. Напишите программу, которая принимает на вход координаты
двух точек и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21.
"""


# Организация выхода
def CheckExit(sign):
    if sign is None or isinstance(sign, bool) and sign:
        print("\nРабота с программой завершена, До встречи!");
        return True
    return False


# Организация ввода и возврат целого числа (в т.ч. отрицательное)
# в заданном диапазоне или выход. C полным контролем корректности
def GetInputNumber(*rang, txt='Введите число', departed=None):
    borders = '' if len(rang) == 0 else f' ({rang[0]} ... {rang[1]}).'
    txt_input = f'{txt}{borders}'
    frm, to = (rang + (None, None))[:2]

    while True:
        key_forCancel = (f'введите "{departed}" или ' if not (departed is None) else '') + '[Enter]'
        numb = input(txt_input + f' (для отказа {key_forCancel}) -> ')

        if not (departed is None) and numb == departed or len(numb) == 0: return None
        try:
            numb = int(numb)
        except ValueError:
            print(f'Введенная строка "{numb}" не является числом. ', end='')
            txt_input = 'Повторите ввод.'
            continue

        if not (frm is None) and numb < frm or not (to is None) and numb > to:
            print(f'Введенное число {numb} должно быть в диапазоне ({rang[0]} ... {rang[1]}) -> ', end='')
            txt_input = 'Повторите ввод.'
            continue

        return numb


# Ввод нескольких целых чисел - Возврат введенных чисел в виде кортежа
def GetInputTuple(*inputParams, departed=None):
    tup_iPar = tuple()
    for param in inputParams:
        inputParam = GetInputNumber(txt=param, departed=departed)
        if inputParam is None: return None
        tup_iPar += (inputParam,)
    return tup_iPar


# Расчет расстояния между 2-мя точками в n-мерной системе координат (nD)
def Distance_TwoPoints(*points):
    sum_ofSquares = 0.00
    nD = int(len(points) / 2)
    for ind in range(0, nD):
        sum_ofSquares += (points[ind + nD] - points[ind]) ** 2
    return round(sum_ofSquares ** (1 / 2), 3)


""" 
==============================================================================================
Основное тело программы
==============================================================================================
"""
print('Расчет расстояния между между точками в 2D пространстве, по заданным координатам:')
while True:
    enterData = GetInputTuple('x1 =', 'y1 =', 'x2 =', 'y2 =', departed='-')
    if CheckExit(enterData):
        break
    x1, y1, x2, y2 = enterData

    distance = Distance_TwoPoints(x1, y1, x2, y2)
    print(f'Расстояние между точками ({x1}, {y1}) и ({x2}, {y2}) в 2D пространстве = {distance}')
    print('\nСледуюшая пара точек ...')
