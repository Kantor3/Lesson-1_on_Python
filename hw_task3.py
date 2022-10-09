"""
Задача-3. Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой
находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
"""


# Организация ввода и возврат целого числа (в т.ч. отрицательное)
# в заданном диапазоне или выход с полным контролем корректности
def GetInputNumber(since=None, to=None, txt='Введите число', departed=None):
    borders = '' if since is None else f' ({since} ... {to}).'
    txt_input = f'{txt}{borders}'

    while True:
        key_forCancel = (f'введите "{departed}" или ' if not (departed is None) else '') + '[Enter]'
        numb = input(txt_input + f' Для отказа {key_forCancel} -> ')

        if not (departed is None) and numb == departed or len(numb) == 0: return None
        try:
            numb = int(numb)
        except ValueError:
            print(f'Введенная строка "{numb}" не является числом. ', end='')
            txt_input = 'Повторите ввод.'
            continue

        if not (since is None) and not (to + 1 > numb > since - 1):
            print(f'Введенное число {numb} должно быть в диапазоне ({since} ... {to}) -> ', end='')
            continue

        return numb


# Основное тело программы
# =============================================================
print('Определяем по координатам точки (X ≠ 0 и Y ≠ 0) '
      'номер четверти плоскости, или ось, где она находится:')

while True:
    X = GetInputNumber(txt='Введие координату X', departed='-')
    if X is None: break
    Y = GetInputNumber(txt='Введие координату Y', departed='-')
    if Y is None: break

    whe_txt = f'точка с координатами ({X}, {Y}) находится '
    if X > 0 and Y > 0: whe = 1
    if X < 0 and Y > 0: whe = 2
    if X < 0 and Y < 0: whe = 3
    if X > 0 and Y < 0: whe = 4
    if X == 0: whe = 'на оси X'
    if Y == 0: whe = 'на оси Y'
    if X == 0 and Y == 0: whe = 'в центре плоскости'

    print(f'{whe_txt} в {whe}-й четверти плоскости' if isinstance(whe, int) else f'{whe_txt} {whe}')

print('\nРабота с программой завершена. До встречи!')
