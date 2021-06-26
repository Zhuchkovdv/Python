# print('Home Work 4')
# print('author - Жучков Дмитрий')
# print('Task 4.2')
# li = (input(f'Введите произвольные числа, разделенные пробелом: ')).split()
# li = list(map(int, li))
# # li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# li_n = [li[i+1] for i in range(len(li)-1) if li[i+1] > li[i]]
# print(li)
# print(li_n)
#
# print('Task 4.3')
# li = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
# print(li)
#
# print('Task 4.4')
# li = (input(f'Введите произвольные числа, разделенные пробелом: ')).split()
# li = list(map(int, li))
# # li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# li_n = [li[el] for el, x in enumerate(li) if li.count(x) == 1]
# print(li)
# print(li_n)
#
# print('Task 4.5')
# from functools import reduce
# # li = [1, 2, 3, 4, 5]
# li = [el for el in range(100, 1001) if el % 2 == 0]
# total = reduce(lambda el, prev_el: el*prev_el, li)
# print(total)
#
# print('Task 4.6')
# from itertools import count, cycle
# my_start = input('Введите начальное значение: ')
# my_end = input('Введите конечное значение: ')
# for el in count(int(my_start)):
#     if el > int(my_end):
#         break
#     print(el)
# li = [el for el in range(int(my_start), int(my_end)+1)]  # туплю, только так криво пересобрал список
# # print(li)
# my_cycle = int(input('Введите количество циклов: '))
# c = 1
# for el in cycle(li):
#     if c > my_cycle:
#         break
#     print(el)
#     c += 1
#
# print('Task 4.7')
# n = int(input('Введите целое число: '))
#
#
# def for_el_in_fact():
#     for i in [el for el in range(1, n + 1)]:
#         yield i
#
#
# g = for_el_in_fact()
# fact = 1
# for elem in g:
#     fact *= elem
#     print(fact)

