# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, list_1):
        self.list_1 = list_1

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.list_1]))

    def __add__(self, other):
        mat = []
        for i in range(len(self.list_1)):
            temp = []
            for j in range(len(self.list_1[i])):
                x = self.list_1[i][j] + other.list_1[i][j]
                temp.append(x)
            mat.append(temp)
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mat]))


my_matrix_1 = Matrix([[5, 18, 11], [6, 17, 23], [41, 50, 9]])
my_matrix_2 = Matrix([[6, 19, 12], [7, 18, 24], [42, 51, 10]])
print(my_matrix_1)
print()
print(my_matrix_2)
print()
print(my_matrix_1 + my_matrix_2)


# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто)
# и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class MyAbCl(ABC):
    @abstractmethod
    def get_amount_c(self):
        pass

    def get_amount_s(self):
        pass

class Cloths(MyAbCl):
    def __init__(self, s, h):
        self.s = s
        self.h = h

    def get_amount_c(self):
        return self.s / 6.5 + 0.5

    def get_amount_s(self):
        return 2 * self.h + 0.3

    @property
    def get_full_amount(self):
        return str(f"Общий раcход ткани: {(self.get_amount_c() + self.get_amount_s())}")


class Coat(Cloths):

    def __str__(self):
        return f"Расход ткани на пальто {self.get_amount_c()}"


class Suit(Cloths):

    def __str__(self):
        return f"Расход ткани на костюм {self.get_amount_s()}"


cloth = Cloths(2, 4)
coat = Coat(2, 4)
suit = Suit(2, 4)
print(coat)
print(suit)
print(cloth.get_full_amount)


# 3. Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам
# и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное)
# деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек
# исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять
# только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки
# определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(),
# принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает,
# то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12,
# количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n**.
# Или, количество ячеек клетки равняется 15,
# количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell:
    def __init__(self, c_amount):
        self.c_amount = int(c_amount)

    def __str__(self):
        return f'({self.c_amount * "*"})'

    def __add__(self, other):
        return Cell(self.c_amount + other.c_amount)

    def __sub__(self, other):
        if (self.c_amount - other.c_amount) > 0:
            return Cell(self.c_amount - other.c_amount)
        else:
            return f"Разность клеток меньше нуля"

    def __mul__(self, other):
        return Cell(self.c_amount * other.c_amount)

    def __truediv__(self, other):
        return Cell(self.c_amount // other.c_amount)

    def make_order(self, cells_r):
        row = ""
        for i in range(round(int(self.c_amount) / cells_r)):
            row += f"({'*' * cells_r})"
        row += f"({'*' * (self.c_amount % cells_r)})"
        return row


cells_1 = Cell(12)
cells_2 = Cell(9)
print(f"1.{cells_1}")
print(f"2.{cells_2}")
print(f"3.{cells_1 + cells_2}")
print(f"4.{cells_1 - cells_2}")
print(f"5.{cells_1 * cells_2}")
print(f"6.{cells_1 / cells_2}")
print(f"7.{cells_1.make_order(10)}")
print(f"8.{cells_2.make_order(2)}")
