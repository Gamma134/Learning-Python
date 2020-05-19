# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time


def running():
    i = 0
    while True:
        while i % 2:
            for el in TrafficLight.__colors:
                if el == "red":
                    print(f"\033[31m {el}")
                    i += 1
                    time.sleep(7)
                elif el == "yellow":
                    print(f"\033[33m {el}")
                    i += 1
                    time.sleep(3)
                elif el == "green":
                    print(f"\033[36m {el}")
                    i += 1
                    time.sleep(7)


class TrafficLight:
    __color = None
    __colors = ["red", "yellow", "green"]

    def __init__(self):
        self.__color = self.__colors[0]


traffic = TrafficLight()
running()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500т


class Road:
    length = None
    width = None

    def __init__(self, length, width, mass, thickness):
        self.thickness = thickness
        self.length = length
        self.width = width
        self.mass = mass
        self.thickness = thickness

    def total_mass(self):
        print(f"To build a road, you need {self.length * self.width * (self.mass / 1000) * self.thickness} tonnes")


mass_count = Road(20, 5000, 25, 5)
mass_count.total_mass()


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary": salary, "bonus": bonus}


class Position(Worker):
    pass

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(self._income.get("salary") + self._income.get("bonus"))


a = Position("Boris", "Johnson", "CFO", 100000, 25000)
a.get_full_name(),
a.get_total_income()


# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} moving")

    def stop(self):
        print(f"{self.name} stopped")

    def turn(self, direction):
        print(f"{self.name} turned to {direction}")

    def show_speed(self):
        print(f"Current speed of {self.name} is {self.speed}")

    def iss_police(self):
        if self.is_police == True:
            print(f"{self.name} is from police")
        if self.is_police == False:
            print(f"{self.name} is NOT a police car")


class TownCar(Car):
    pass

    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} exceeded  speed limit by {self.speed - 60} total speed: {self.speed}")
        else:
            print(f"{self.name} speed is {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    pass

    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} exceeded  speed limit by {self.speed - 60} total speed: {self.speed}")
        else:
            print(f"{self.name} speed is {self.speed}")


class PoliceCar(Car):
    pass


ford = TownCar(62, "black", "Ford", False)

ford.show_speed()
ford.turn("City")
ford.iss_police()
ford.stop()
ford.go()
print()

sport = SportCar(180, "red", "Ford", False)

sport.show_speed()
sport.turn("Highway")
sport.iss_police()
sport.stop()
sport.go()
print()

work1 = WorkCar(90, "white,", "Ford", False)

work1.show_speed()
work1.turn("City")
work1.iss_police()
work1.stop()
work1.go()
print()

work2 = WorkCar(90, "white", "Audi", False)

work2.show_speed()
work2.turn("Lake")
work2.iss_police()
work2.stop()
work2.go()
print()

police = PoliceCar(180, "red", "Ford", True)

police.show_speed()
police.turn("Downtown")
police.iss_police()
police.stop()
police.go()


# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Starting to draw")


class Pen(Stationery):
    pass

    def draw(self):
        print(f"Starting to draw with a Pen, title: {self.title}")


class Pencil(Stationery):
    pass

    def draw(self):
        print(f"Starting to draw with a Pencil, title: {self.title}")


class Handle(Stationery):
    pass

    def draw(self):
        print(f"Starting to draw with a handle, title: {self.title}")


pen = Pen('Picture')
pencil = Pencil('Landscape')
handle = Handle('Sky')
pen.draw()
pencil.draw()
handle.draw()
