'''
Задача-2. апишите программу для. проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
'''

# Преобразование в двоичную систему счисления
def Dec_toBinary(numb10, base=2):
    tup_bin = tuple()
    while numb10:
        tup_bin += (numb10 % base,)
        numb10 = numb10 // base
    result = ((0, 0, 0) + tup_bin)[len(tup_bin):]
    return tuple([ind == 1 for ind in result])

# Основное тело программы
# =============================================================
print('Проверяем истинность утверждения\n ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат:')

for i in range(0, 8):
    pr = Dec_toBinary(i)
    l_side = not (pr[0] or pr[1] or pr[2])
    r_side = not pr[0] and not pr[1] and not pr[2]

    truth_stat = 'истинно' if l_side == r_side else 'ложно'

    print(f'{i + 1} (X,  Y,  Z) = (', end='')
    print(*pr, end='')
    print(f') -> {truth_stat}')
