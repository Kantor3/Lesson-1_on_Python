"""
Задача-4. Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
"""

# Организация ввода и возврат целого числа (в т.ч. отрицательное)
# в заданном диапазоне или выход с полным контролем корректности
def GetInputNumber(*rang, txt='Введите число', departed=None):
    borders = '' if len(rang) == 0 else f' ({rang[0]} ... {rang[1]}).'
    txt_input = f'{txt}{borders}'
    fr, to = rang

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

        if not (fr is None) and numb < fr or not (to is None) and numb > to:
            print(f'Введенное число {numb} должно быть в диапазоне ({rang[0]} ... {rang[1]}) -> ', end='')
            txt_input = 'Повторите ввод.'
            continue

        return numb


# Основное тело программы
# =============================================================
print('По указанному номеру четверти коорд. плоскости определяем и возвращаем \n'
      'диапазон возможных координат точек в этой четверти (x и y):')

while True:
    quarter = GetInputNumber(1, 4, txt='Введите номер четверти координатной плоскости', departed='-')
    if quarter is None: break

    quarter -= 1
    rang_txt  = f'\nв {quarter}-й четверти возможны следующие диапазоны координат точек:'
    axisX_txt = f'{(">", "<", "<", ">")[quarter]} 0'
    axisY_txt = f'{(">", ">", "<", "<")[quarter]} 0'

    print(f'{rang_txt}')
    print(f'по оси X -> (X {axisX_txt})')
    print(f'по оси Y -> (Y {axisY_txt})')
    print()

print('\nРабота с программой завершена. До встречи!')