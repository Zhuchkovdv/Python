# print('Home Work 5')
# print('author - Жучков Дмитрий')
# print('Task 5.1')
# file_name = input('Enter name of new file: ')
# f = open(file_name, 'w', encoding='utf-8')
# while True:
#     s = input('Write any text to stroke, '
#               'for another stroke "Enter", '
#               'for stop tap "Enter" with empty stroke: ')
#     if s == '':
#         break
#     f.writelines(s + '\n')
# f.close()
#
# print('Task 5.2')
# with open(r'File5_2.txt', 'r', encoding='utf-8') as f:
#     line = 0
#     for i in f:
#         line += 1
#         word = 0
#         x = 0
#         for k in i:
#             if k != ' ' and x == 0:
#                 word += 1
#                 x = 1
#             elif k == ' ':
#                 x = 0
#         print(i, end='')
#         print('Слов в строке -', word)
#     print('Итого строк -', line)
#
# print('Task 5.3')
# dict = {}
# s = 0
# n = 0
# f = open(r'File5_3.txt', 'r', encoding='utf-8')
# for line in f:
#     (name, salary) = line.split(' ')
#     dict[name] = int(salary)
#     s += int(salary)
#     n += 1
# # print(dict)
# for i in dict:
#     if dict[i] < 20000:
#         print(i)
# avr = s / n
# print(avr)
# f.close()
#
# print('Task 5.4')  # не понял задачу
# dict = {}
# rus = ['Один-1', 'Два-2', 'Три-3', 'Четыре-4']
# r = open(r'File5_4.txt', 'r', encoding='utf-8')
# for line in r:
#     (word, num) = line.split('-')
#     dict[num[:-1]] = word
# # print(dict)
# w = open(r'File5_4_1_rus.txt', 'w', encoding='utf-8')
# for line in rus:
#     w.write(line + '\n')
# r.close()
# w.close()
# print('Task 5.4')  # может так?
# eng = {}
# rus = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
# r = open(r'File5_4.txt', 'r', encoding='utf-8')
# for line in r:
#     (word, num) = line.split('-')
#     eng[num[:-1]] = word
# print(eng)
# w = open(r'File5_4_2_rus.txt', 'w', encoding='utf-8')
# eng.update(rus)
# print(eng)
# s = eng.items()
# print(s)
# for item in s:
#     w.write(str(item) + '\n')
# r.close()
# w.close()
#
# print('Task 5.5')
# file_name = input('Enter name of new file: ')
# with open(file_name, 'w+', encoding='utf-8') as f:
#     f.write(input('Write any numbers from space for sum: ') + ' ')
#     f.seek(0)
#     num = f.read().split()
#     total = 0
#     try:
#         for i in num:
#             total = sum(map(int, num))
#     except ValueError:
#         print('Need a numbers only')
# #    print(num)
#     print('Total: ', total)
#
# print('Task 5.6')
# #
# #
# # def num_returner():
# #     s = []
# #     for num in s:
# #         if 60 <= ord(num) <= 71:
# #             s.append(int(num))
# #
# #
# dict = {}
# s = []
# f = open(r'File5_6.txt', 'r', encoding='utf-8')
# for line in f:
#     (course, lecture, lab, practice) = line.split(' ')
#     l = len(line)
#     s = []
#     i = 0
#     while i < l:
#         s_int = ''
#         x = line[i]
#         while '0' <= x <= '9':
#             s_int += x
#             i += 1
#             if i < l:
#                 x = line[i]
#             else:
#                 break
#         i += 1
#         if s_int != '':
#             s.append(int(s_int))
#     # for num in line: '''Короткий вариант не получился почему-то'''
#     #     if 60 <= ord(num) <= 71:
#     #         s.append(int(num))
#     #         print(num)
#     dict[course] = sum(s)
#     # print(line, end='')
# print(dict)
#
# print('Task 5.7')
# import json
# dict_f = {}
# dict_avr = {}
# s = 0
# n = 0
# f = open(r'File5_7.txt', 'r', encoding='utf-8')
# for line in f:
#     (name, form, income, costs) = line.split(' ')
#     dict_f[name] = int(income) - int(costs)
#     if int(income) - int(costs) > 0:
#         s += int(income) - int(costs)
#         n += 1
# avr = s / n
# dict_avr['average_profit'] = int(avr)
# li = [dict_f, dict_avr]
# print(li)
# f_j = open(r'File5_7.json', 'w')
# json.dump(li, f_j)
# f_j.close()
# f.close()
# print('Task 5.7 - with менеджером контекста')
# import json
# dict_f = {}
# dict_avr = {}
# s = 0
# n = 0
# with open(r'File5_7.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         (name, form, income, costs) = line.split(' ')
#         dict_f[name] = int(income) - int(costs)
#         if int(income) - int(costs) > 0:
#             s += int(income) - int(costs)
#             n += 1
#     avr = s / n
#     dict_avr['average_profit'] = int(avr)
#     li = [dict_f, dict_avr]
#     print(li)
#     with open(r'File5_7.json', 'w') as f_j:
#         json.dump(li, f_j)
