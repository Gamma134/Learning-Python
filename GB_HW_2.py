# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_list = []
my_list.append(1)
my_list.append(True)
my_list.insert(2, "Hi")
my_list.append(.345345)
my_list.insert(3, [1, 2, 3])

print(my_list)
print()
for i in my_list:
    print(f"{type(i)} - {i}")
print()
# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


a = [i for i in input("Enter value with space: ").split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))
print()
# Чуть не сгорел пока писал код :c.

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.


s_dict = {1: "Winter", 2: "Spring", 3: "Summer", 4: "Autumn"}
s_list = ["Winter", "Spring", "Summer", "Autumn"]

month_s = int(input("Please enter month's numeric: "))
if month_s == 1 or month_s == 2 or month_s == 3:
    print(f"List: {s_list[0]}")
    print(f"Dictionary: {s_dict.get(1)}")
elif month_s == 4 or month_s == 5 or month_s == 6:
    print(f"List: {s_list[1]}")
    print(f"Dictionary: {s_dict.get(2)}")
elif month_s == 7 or month_s == 8 or month_s == 9:
    print(f"List: {s_list[2]}")
    print(f"Dictionary: {s_dict.get(3)}")
elif month_s == 10 or month_s == 11 or month_s == 12:
    print(f"List: {s_list[3]}")
    print(f"Dictionary: {s_dict.get(4)}")
else:
    print("Wrong value, try again!: ")
print()
# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
u_input = input("Please enter words with spaces between them: ").split()
for i, el in enumerate(u_input, 1):
    if len(el) > 10:  # Ограничитель кол-ва слов
        print(i, el[:9])
    else:
        print(i, el)
print()
# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

r_list = [7, 5, 3, 3, 2]
u_a = int(input("Please enter a value for the ranking: "))
for i in range(len(r_list)):
    if r_list[i] == u_a:
        r_list.insert(i + 1, u_a)
        break
    elif r_list[-1] > u_a:
        r_list.append(u_a)
        break
    elif r_list[0] < u_a:
        r_list.insert(0, u_a)
        break
    elif r_list[i] > u_a > r_list[i + 1]:
        r_list.insert(i + 1, u_a)
        break
print(r_list)
print()
# 6.Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.


inventory = int(input("Please enter the amount of goods you want to add: "))
n = 1
inv_list = []
inv_dir = {}
analysis = {}
while n <= inventory:
    inv_dir = dict({"Name": input("Good's name?: "), "Price": input("Good's price?: "),
                    "Amount": input("What amount?:"), "Unit": input("Unit of measure?: ")})
    inv_list.append((n, inv_dir))
    n += 1
    analysis = dict({"Name": inv_dir.get("Name"), "Price": inv_dir.get("Price"), "Amount": inv_dir.get("Amount"),
                     "Unit": inv_dir.get("Name")})
print(inv_list)
print(analysis)
#FIn
