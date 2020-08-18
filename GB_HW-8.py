# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        result = []

        for i in day_month_year.split("-"):
            my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])  # Хотел попробовать вывести черещ "map",
        # но что-то пошло не так

    @staticmethod
    def check(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2020:
                    return "Date values are correct"
                else:
                    return "Year values are incorrect"
            else:
                return "Month values are incorrect"
        else:
            return "Day values are incorrect"

    def __str__(self):
        return f"Entered date is {Date.extract(self.day_month_year)}"


date = Date("11-5-13")
print(date)
print(Date.check(7, 5, 2024))
print(date.check(11, 14, 2019))
print(Date.check(22, 10, 1991))
print(Date.extract('08-11-2018'))



# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class DivisionNull:
    def __init__(self, numerator, denominator):
        self.divider = numerator
        self.denominator = denominator

    @staticmethod
    def division(numerator, denominator):
        try:
            return (numerator / denominator)
        except:
            return (f"Zero division not allowed")


div = DivisionNull(10, 100)
print(div.division(100, 0))
print(DivisionNull.division(10, 0))


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class My_Exception(Exception):
    def __init__(self, *args):
        self.txt = []

    def u_input(self):
        while True:
            try:
                val = int(input("Please enter value with Enter: "))
                self.txt.append(val)
                print(f"Current list: {self.txt}")
            except:
                print(f"Only numbers are allowed")
                choice = input("Want to try again? (Y/N)? ").capitalize()

                if choice == "Y":
                    print(check.u_input())
                elif choice == "N":
                    return "Exiting"
                else:
                    return "Exiting"


check = My_Exception()
print(check.u_input())

# 4, 5, 6
"""class Inventory:
    def __init__(self, *args):
        self.inv = {}
        self.whole = []

class OfficeEquipment(Inventory):
    def __init__(self, model, price, quantity, *args):
        self.model = model
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.model}, price: {self.price}, in stock: {self.quantity}"

    def stock_management(self):
        try:
            unit = input(f"Enter a model name: ")
            uprice = int(input("Enter unit price: "))
            uqantity = int(input("Enter amount: "))
        except:
            pass

        ans =input("Enter 'Q' or 'q' to exit or 'Enter' to continue").capitalize()
        if ans == "Q":
            self.whole.append(self.inv)
            print(f"Whole stock \n {self.whole}")
            return "Exiting"
        else:
            return OfficeEquipment.stock_management(self)

class Printer(OfficeEquipment):
    
        

class Scanner(OfficeEquipment):
   

class Xerox(OfficeEquipment):
   """

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    def __init__(self, n_1, n_2):
        self.n_1 = n_1
        self.n_2 = n_2

    def __add__(self, other):
        return f"answer = {self.n_1 + other.n_1} + {self.n_2 + other.n_2} * i"

    def __mul__(self, other):
        return f"answer = {self.n_1 * other.n_1} + {self.n_2 * other.n_2} * i"

    def __str__(self):
        return f"answer = {self.n_1} + {self.n_2} * i"


q_1 = Complex(1, -8)
q_2 = Complex(9, 5)
print(q_1)
print(q_2)
print(q_1 + q_2)
print(q_1 * q_2)

# Никогда не работал с комплексными числам и не уверен правильно ли все сделал :'D

