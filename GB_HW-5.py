# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open("text_1", "w+", encoding="utf-8") as my_file:
    while input("Press 'Enter' to continue or 'Q' to exit: ").capitalize() != "Q":
        print(input("Введите данные для записи в файл: "), file=my_file)

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


with open("text_2") as my_file:
    lines = 0
    letters = 0
    x = 1
    for line in my_file:
        lines += line.count("\n")
        letters = len(line) - line.count(" ") - 1
        print(f"{x} line: {letters} letters in line")
        x += 1
    print()
    print(f"String count is: {lines}")

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.


with open("text_3.txt", "r", encoding="utf-8") as my_file:
    employee = {}
    for line in my_file:
        key, value = line.split()
        employee[key] = value
        if float(value) < 20000:
            print(f"{key}: имеет зарплату меньше 20 тысяч. Текушая зарплата: {value}")

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыри"}
translation = []
with open("text_4.txt", "r", encoding="utf") as my_file:
    for line in my_file:
        line = line.split(" ", 1)
        translation.append(translate[line[0]] + " " + line[1])
    print(translation)
with open("text_4(rus).txt", "w", encoding="utf-8") as my_file2:
    my_file2.writelines(translation)


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def sum_n():
    try:
        with open("text_5.txt", "w+", encoding="utf-8") as my_file:
            numbers = input("Enter numbers with spaces:")
            my_file.writelines(numbers)
            number = numbers.split()
            print(sum(map(int, number)))
            my_file.close()
    except IOError:
        print("File error")
    except ValueError:
        print("Use numbers only!")


sum_n()

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий
# по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —

# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open("text_6.txt", "r", encoding="utf-8") as my_file:
    subjects = {}
    for line in my_file:
        subject, lecture, practice, lab = line.split()
        lectures = lecture, practice, lab
        s = line
        l = len(s)
        integ = []
        i = 0
        while i < l:
            s_int = ''
            a = s[i]
            while '0' <= a <= '9':
                s_int += a
                i += 1
                if i < l:
                    a = s[i]
                else:
                    break
            i += 1
            if s_int != '':
                integ.append(int(s_int))
            subjects[subject] = sum(integ)
print(f"Total number of hours per subject: {subjects}")

# 7. Создать (не программно) текстовый файл, в котором
# каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

firm_lst = []
firm_dir = {}
all_avg = {}
profit = 0
avg_profit = 0
i = 0
with open("text_7.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        name, firm, earning, damage = line.split()
        firm_dir[name] = int(earning) - int(damage)
    for name in firm_dir:
        if firm_dir[name] >= 0:
            profit = profit + firm_dir[name]
            i += 1

if i != 0:
    avg_profit = profit / i
    print(f"Средний дохож компания - {avg_profit:.2f}")

all_avg = {"Средняя прибыль": round(avg_profit)}
firm_dir.update(all_avg)
firm_lst.append(firm_dir)
print(f"Прибыль каждой компании - {firm_lst}")

with open("file_7.json", "w", encoding="utf-8") as my_js:
    json.dump(firm_lst, my_js)
    js_str = json.dumps(firm_lst)
    print(f"json : {js_str}")

# Есть проблема с отображением Кириллицы.
# Нашел решение через "JSON_UNESCAPED_UNICODE" правда так и не смог интегрировать.
