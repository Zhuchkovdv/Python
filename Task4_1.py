from sys import argv
print('Home Work 4')
print('author - Жучков Дмитрий')
print('Task 4.1')
try:
    path, name, hours_work, pay_hours, award = argv
    hours_work, pay_hours, award = map(int, argv[2:])
    total = hours_work * pay_hours + award
    print("Имя работника: ", name)
    print("Отработано часов: ", hours_work)
    print("Ставка за час: ", pay_hours)
    print("Премия: ", award)
    print("Итого: ", total)
except ValueError:
    print("Неправильное количество параметров")



