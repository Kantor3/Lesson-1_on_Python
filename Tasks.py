'''
Задача 1.
Написать программу, которая принимает на вход два целых числа и проверяет, 
является ли одно число квадратом другого.
Примеры
5, 25 -> да
4, 16 -> да
25, 5 -> да
8,9 -> нет
'''
# print('Определим является ли одно число (A) квадратом другого (B) \n')
# print('Введите 2-а числа (A и B), для завершения введите "0" :\n')

# while True:

#     A = int(input("A = "))
#     # if not A.isdigit():
#     #     continue
#     if A == 0:
#         break

#     B = int(input("B = "))
#     if B == 0:
#         break

#     if B**2 == A:
#         print("-> да")
#     else:
#         print("-> нет")

# print('Работа с программой завершена. До встречи!')

'''
Задача 2.
Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
Примеры:
1, 4, 8, 7, 5 -> 8
78, 55, 36, 90, 2 -> 90
'''
# print('Ищем максимальное число из 5 введенных \n')
# list_number = []

# for i in range(5):
#     list_number.append(int(input()))

# max_number = list_number[0]
# for el in list_number:
#     max_number = max(el, max_number)

# print('Введены числа: ', *list_number)
# print(f'\n Максимальное число из введенных чисел -> {max_number}')

'''
Задача 3.
Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
Примеры:
5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
'''
# N = int(input("Введите целое число -> "))
# print( *([i for i in range(-N, N+1)]) )

'''
Задача 4.
Напишите программу, которая принимает на вход число и проверяет, 
кратно ли оно 5 и 10 или 15, но не 30.
'''
# N = int(input("Введите целое число -> "))
# result = "Условие выполняется" if (N % 5 == 0) and (N % 10 == 0) or (N % 15 == 0) or not (N % 30 == 0) else "Условие не выполняется"
# print(result)

'''
Задача 5.
Напишите программу, которая будет принимать на вход дробь и 
показывать первую цифру дробной части числа.
Примеры
6.78 -> 7
5 -> нет
0.34 -> 3
'''

N = float(input("\nВведите дробь (в форме 'NNN.NNN') -> "))
temp = N * 10
temp = temp - temp % 1
temp = int(round( ((temp / 10) % 1) * 10, 0))

print(f'Первая цифра дробной части -> {temp}')

