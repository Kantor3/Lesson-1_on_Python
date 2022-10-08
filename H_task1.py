'''
Напишите программу, которая принимает на вход цифру,
обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
'''

# Организация ввода и возврат числа в заданном диапазоне с полным контролем
def GetInputNumber(since, to, txt = 'Введите число (для отказа [Enter])', exit=None):

    print(f'{txt} ({since} ... {to}): ', end='')
    while True:

        number = input()

        if not (exit is None) and number == exit or len(number) == 0: return None
        if not number.isdigit():
            print(f'Введенная строка "{number}" не является числом')
            print('Повторите ввод. Для отказа [Enter] -> ', end='')
            continue

        number = int(number)
        if not to+1 > number > since-1:
            print(f'Введенное число {number} должно быть в диапазоне ({since} ... {to}) -> ', end='')
            continue

        return  number


# Тело программы
print('Определяем является ли указанный день недели выходным:')

while True:

    number = GetInputNumber(1, 7, exit='0')
    if number is None: break
    print(f'- {number} -> { "да" if number in [6, 7] else "нет"}')
