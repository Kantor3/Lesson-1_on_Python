"""
Задача-1. Напишите программу, которая принимает на вход цифру,
обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
"""


# Организация ввода и возврат числа в заданном диапазоне с полным контролем
def GetInputNumber(since, to, txt='Введите число (для отказа [Enter])', departed=None):
    print(f'{txt} ({since} ... {to}): ', end='')
    while True:

        numb = input()

        if not (departed is None) and numb == departed or len(numb) == 0: return None
        if not numb.isdigit():
            print(f'Введенная строка "{numb}" не является числом')
            print('Повторите ввод. Для отказа [Enter] -> ', end='')
            continue

        numb = int(numb)
        if not to + 1 > numb > since - 1:
            print(f'Введенное число {numb} должно быть в диапазоне ({since} ... {to}) -> ', end='')
            continue

        return numb


# Тело программы
# =============================================================
print('Определяем является ли указанный день недели выходным:')

while True:

    number = GetInputNumber(1, 7, departed='0')
    if number is None: break
    print(f'- {number} -> {"да" if number in [6, 7] else "нет"}')
