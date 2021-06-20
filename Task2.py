# print('Home Work 2')
# print('author - Жучков Дмитрий')

# print('Task 2.1.1 #while-method')
# li = [5, 9.7, 'x', 'word', [3, 85, 'm'], False]
# print(li)
# e = len(li) # количество элементов списка
# print(e)
# i = 0
# while i != e:
#     print(type(li[i]))
#     i += 1
# print('Task 2.1.1 #for_in-method')
# li = [5, 9.7, 'x', 'word', [3, 85, 'm'], False]
# print(li)
# for el in li:
#     print(type(el), el)

# print('Task 2.2')
# s1 = (input('Enter any symbols using space: ')).split() # запрос данных и преобразование их в список
# print(s1)
# e = len(s1) # количество элементов списка
# print(e)
# f = 0 #первый член пары
# s = 1 #второй
# while s != e:
#     s1[f], s1[s] = s1[s], s1[f]
#     f += 2
#     s = f + 1
# print(s1)

# print('Task 2.3.1 #dict-method')
# di = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}
# num = int(input(f'Enter a number of month from 1 to 12: '))
# for key in di:
#     if num == key:
#          print(f'The season is {di[key]}')
#          break
# print('Task 2.3.1 #list-method')
# num = int(input(f'Enter a number of month from 1 to 12: '))
# li = [1, 'Winter', 2, 'Winter', 3, 'Spring', 4, 'Spring', 5, 'Spring', 6, 'Summer', 7, 'Summer', 8, 'Summer', 9, 'Autumn', 10, 'Autumn', 11, 'Autumn', 12, 'Winter']
# for el in li:
#     if num == el:
#         i = li.index(el)
#         i += 1
#         print(f'The season is {li[i]}')
#         break

# print('Task 2.4')
# s1 = (input('Enter any words using space: ')).split() # запрос данных и преобразование их в список
# #print(s1)
# for ind, el in enumerate(s1, 1):
#     print(ind, el[0:10])

# print('Task 2.5')
# my_list = [7, 5, 3, 3, 2]
# print(my_list)
# num = int(input(f'Enter any number from 0 to 9: '))
# my_list.append(num)
# my_list.sort()
# my_list.reverse()
# print(my_list)

print('Task 2.6*')
print(f'Введите данные по группе товаров, для завершения ввода введите "done"')
tab = []
i = 0
names = {}
price = {}
quantity = {}
measure = {}
while True:
    item = input("Название: ")
    if item == 'done':
        break
    names['Название'] = item
    p = int(input("Цена: "))
    price['Цена'] = p
    q = int(input("Количество: "))
    quantity['Количество'] = q
    m = input("Ед: ")
    measure['Ед'] = m
    i += 1
    good = []
    good.append(i)
    good.append({**names, **price, **quantity, **measure})
    a = tuple(good)
    tab.append(good)
    print(a)
# print(len(tab))
print(tab)
print('Больше ничего не успел((')

