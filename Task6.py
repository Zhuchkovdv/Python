# print('Home Work 6')
# print('author - Жучков Дмитрий')
# print('Task 6.1')
# import time
#
#
# class Trafficlight:
#
#     def __init__(self, color, timer):
#         self.__c = color
#         self._t = timer
#         # print(f'Color: {self.__c}, timer: {self._t}')
#
#     def running(self):
#         print(f'Загорелся {self.__c} свет')
#         time.sleep(self._t)
#
#
# red = Trafficlight('красный', 7)
# red.running()
#
# yellow = Trafficlight('желтый', 2)
# yellow.running()
#
# green = Trafficlight('зеленый', 6)
# green.running()
#
# print('Task 6.2')
# th = int(input('Введите толщину слоя асфальта в см: '))
# _l = int(input('Введите длину дороги в м: '))
# _w = int(input('Введите ширину дороги в м: '))
#
#
# class Road:
#
#     def __init__(self, length, width):
#         self._l = length
#         self._w = width
#         # print(f' length: {self._l}, width: {self._w}')
#
#     def massing(self):
#         mass = self._l * self._w * 0.025 * th
#         print(f'Масса асфальта в тоннах: {mass}т')
#
#
# r = Road(_l, _w)
# r.massing()
#
# print('Task 6.3')
#
# n = input('Имя: ')
# sn = input('Фамилия: ')
# p = input('Должность: ')
# w = int(input('Оклад: '))
# b = int(input('Премия: '))
# dict_income = {'wage': w, 'bonus': b}
# _i = dict_income
#
#
# class Worker:
#
#     def __init__(self, name, surname, position, income):
#         self.n = name
#         self.sn = surname
#         self.p = position
#         self._i = income
#         # print(f'Name: {self.n}, Surname: {self.sn}, Position: {self.p}, Income: {self._i}')
#
# class Position(Worker):
#
#     def get_full_name(self):
#         print(f'{p}: {sn} {n}')
#
#     def get_total_income(self):
#         _i = sum(dict_income.values())
#         print(f'Итого доход: {_i}')
#
#
# emp = Worker(n, sn, p, _i)
# emp1 = Position(n, sn, p, _i)
# emp1.get_full_name()
# emp1.get_total_income()
#
# print('Task 6.4')
# class Car:
#
#     def __init__(self, name, color, speed, is_police):
#         self.n = name
#         self.c = color
#         self.s = speed
#         self.p = is_police
#         print(f'Name: {self.n}, Color: {self.c}, Speed: {self.s}, Police: {self.p}')
#
#     def go(self):
#         print(f'{self.n} едет')
#
#     def stop(self):
#         print(f'{self.n} стоит')
#
#     def turn(self):
#         print(f'{self.n} повернул(а)')
#
#     def show_speed(self):
#         print(f'Скорость {self.n} составляет {self.s} км/ч')
#
#
# class TownCar(Car):
#     def show_speed(self):
#         if self.s > 60:
#             print(f'Разрешенная для {self.n} скорость в 60 км/ч превышена!')
#         else:
#             print(f'Скорость {self.n} составляет {self.s} км/ч')
#
#
# class SportCar(Car):
#     pass
#
#
# class WorkCar(Car):
#     def show_speed(self):
#         if self.s > 40:
#             print(f'Разрешенная для {self.n} скорость в 40 км/ч превышена!')
#         else:
#             print(f'Скорость {self.n} составляет {self.s} км/ч')
#
#
# class PoliceCar(Car):
#     pass
#
#
# car1 = TownCar('Lada X-ray', 'Red', 75, False)
# car1.go()
# car1.stop()
# car1.show_speed()
# car1.turn()
# car2 = SportCar('Lamborghini Huracan', 'Yellow', 120, False)
# car2.go()
# car2.stop()
# car2.show_speed()
# car2.turn()
# car3 = WorkCar('JCB Fastrac', 'Blue', 47, False)
# car3.go()
# car3.stop()
# car3.show_speed()
# car3.turn()
# car4 = PoliceCar('Sкoda Octavia', 'White', 95, True)
# car4.go()
# car4.stop()
# car4.show_speed()
# car4.turn()
# car5 = TownCar('Volkswagen Tiguan', 'Blue', 55, False)
# car5.go()
# car5.stop()
# car5.show_speed()
# car5.turn()
# car6 = WorkCar('Komatsu GD705-5', 'Black', 32, False)
# car6.go()
# car6.stop()
# car6.show_speed()
# car6.turn()
#
# print('Task 6.5')
#
# class Stationery:
#
#     def __init__(self, title):
#         self.t = title
#         print(f'Title: {self.t}')
#
#     def draw(self):
#         print('Запуск отрисовки.')
#
#
# class Pen(Stationery):
#
#     def draw(self):
#         print('Запуск отрисовки ручкой.')
#
#
# class Pencil(Stationery):
#
#     def draw(self):
#         print('Запуск отрисовки карандашом.')
#
#
# class Handle(Stationery):
#
#     def draw(self):
#         print('Запуск отрисовки маркером.')
#
#
# it1 = Pen('Parker')
# it1.draw()
# it2 = Pencil('KOH-I-NOOR')
# it2.draw()
# it3 = Handle('COPIC')
# it3.draw()
