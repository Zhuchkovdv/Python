# print('Home Work 3')
# print('author - Жучков Дмитрий')

# print('Task 3.1')


# def my_del(arg1, arg2):
#     res = arg1 / arg2
#     return res
#
#
# a = int(input('Enter num1: '))
# b = int(input('Enter num2: '))
# try:
#     result = my_del(a, b)
#     print(result)
# except ZeroDivisionError:
#     print('Нельзя делить на ноль')
#
# print('Task 3.2')
#
#
# def user(name, s_name, year_b, city, mail, tel):
#     res = ' '.join([name, s_name, year_b, city, mail, tel])
#     return res
#
#
# print(f'Введите данные о пользователе, для завершения ввода введите "end"')
# while True:
#     name = str(input('Имя: '))
#     if name == 'end':
#         break
#     s_name = str(input('Фамилия: '))
#     year_b = str(input('Год рождения: '))
#     city = str(input('Город проживания: '))
#     mail = str(input('Email: '))
#     tel = str(input('Телефон: '))
#     a = user(name, s_name, year_b, city, mail, tel)
#     print(a)
#
# print('Task 3.3')
#
#
# def two_of_three(a, b, c):
#     return a + b + c - min(a, b, c)
#
#
# a = int(input('noun1: '))
# b = int(input('noun2: '))
# c = int(input('noun3: '))
# s = two_of_three(a, b, c)
# print(s)

# print('Task 3.4.1') #"for in-method"
#
#
# def my_power(x, y):
#     res = 1
#     for i in range(abs(y)):
#         res *= 1 / x
#     return res
#
#
# x = int(input('Действительное положительное число: '))
# y = int(input('Целое отрицательное число: '))
# a = my_power(x, y)
# print(a)

# print('Task 3.4.2') #"**-method"
#
#
# def my_power(x, y):
#     res = 1 / x ** abs(y)
#     return res
#
#
# x = int(input('Действительное положительное число: '))
# y = int(input('Целое отрицательное число: '))
# a = my_power(x, y)
# print(a)
#
# print('Task 3.5') """Не выполнена((("""


# def stop(*a):
#     global total
#     for a in li:
#         if a == 'stop':
#             li.pop()
#             total = sum(map(int, li))
#             break
#     total = sum(map(int, li))
#
#     return li, total


# while True:
#         li = (input(f'Введите числа, разделенные пробелом, для нахождения суммы нажмите "Enter", '
#                     f'для завершения ввода введите "stop и "Enter": ')).split()
#         total = sum(map(int, li))
#         print(li)
#         print(total)
#         li.extend(li)
#         print(li)
#         print(total)

# print('Task 3.6.1') #"one word"
#
#
# def int_func(w):
#     w = w.title()
#     return w
#
#
# word = (input('Enter any word: '))
# print(word)
# s = int_func(word)
# print(s)

# print('Task 3.6.2')  # "full stroke"
#
#
# def int_func(w):
#     w = w.title()
#     return w
#
#
# s = (input('Enter any words from space: ').split())
# s = list(map(int_func, s))
# s = ' '.join(s)
# print(s)
