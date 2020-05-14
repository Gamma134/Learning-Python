# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y can not be zero"
    except ValueError:
        return "Only number are excepted"


print(my_func(int(input("Enter value for 'x': ")), int(input("Enter value for 'y': "))))


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, b_date, city, email, phone):
    print(name, surname, b_date, city, email, phone)


my_func(input("Enter your name: "), input("Enter your surname: "), int(input("Enter the year you was born:?")),
        input("Enter the city you was born in: "), input("Please enter your email: "), input("Please enter your phone:\
 "))


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    l = [x, y, z]
    sum_l = []
    max_1 = max(l)
    sum_l.append(max_1)
    l.remove(max_1)
    max_2 = max(l)
    sum_l.append(max_2)
    print(sum(sum_l))


my_func(int(input("Input first value: ")), int(input("Enter second value: ")),
        int(input("Input third value: ")))


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# 4.1
def my_func(x, y):
    return 1 / x ** abs(y)


print(my_func(int(input("Input first value: ")), int(input("Enter second value: "))))


# 4.2

def my_power(a, n):
    n = 1
    for i in range(abs(n)):
        n *= a
    if n >= 0:
        return n
    else:
        return 1 / n


print(my_power(float(input("Enter the first number ")), int(input("Enter the second number: "))))


# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.

def my_sum():
    sum_n = 0
    i = False
    while i == False:
        number = input("Input numbers with spaces between them or 'Q' (quit) to exit the program: ").split()

        n = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                i = True
                break
            else:
                n = n + int(number[el])
        sum_n = sum_n + n
        print(f'Current sum is {sum_n}')
    print(f'Your final sum is {sum_n}')


my_sum()


# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def my_func(*args):
    word = input("Input words: ")
    print(word.title())
    return


my_func()
