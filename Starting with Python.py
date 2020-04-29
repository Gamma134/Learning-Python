# Py:Урок_1 Практическое задание
# 1.1 Работа с переменными

var_1 = "Hello"
var_2 = "World"
n_var_1 = 10
n_var_2 = 0.43
n_var_3 = 17

a = var_1 +" "+ var_2 # Текстовые переменные
print(a)

b = n_var_1 + n_var_2 + n_var_3 # Числовые переменные
print (b)


user_input_1 = input("Please input a number: ") # Запрос на ввод данных
print("You have entered: " + user_input_1 + ", value saved!")
print()

# 2. Ввод времени в секундах и отображение в HH:MM:SS формате
time_s = int(input("Please enter time in second: "))
hh = (time_s // 3600) # Перевод в часы
mm = (time_s//60) % 60 # Перевод в остаток минут
ss = (time_s % 60) # Перевод в остаток секунд
if mm<10: # Правильное отображение минут
    mm= str("0"+str(mm))
else:
    mm=str(mm)
if ss<10: # Правильное отображение секунд
    ss=str("0"+str(ss))
else:
    ss = str(ss)

print(f"{hh}:{mm}:{ss}") # Вывод
print()

#3. Ввод чистла для вывода в формате n+nn+nnn
n = int(input("Enter a number to see it n+nn+nn format: "))# Запрос ввода
n_answer = n+((n*10)+n)+((n*100)+(n*10)+n)# Решение уровнения

print(f"{n}+{n}{n}+{n}{n}{n} = {n_answer}") #Вывод в требуемом формате
print()

#4. Нахождение самой большой цифры из целого числа с использовагием цикла while.
n_input = int(input("Please enter the whole figure to find the largest number in it: "))
n = 0
max_n = 0
while n_input > 0:
    n = n_input % 10
    n_input = n_input // 10
    if max_n < n:
        max_n = n
        continue
print(max_n)
print()

#5. Форма для фирмы
earn = int(input("Please enter the earning amount: "))
exp =  int(input("Please enter the expenses amount: "))
ops = earn - exp

if earn > exp:
    print (f"Congratulations! Your profit: {ops}")
    print(f"Your profitability is: {ops/earn}")
    emp = int(input("Please enter the number of employees in your company: "))
    print (f"Your profit per employee is: {ops/emp}")
elif earn < exp:
    print(f"You are at breakeven. Your profit: {ops}")
else:
    print(f"Your loss is: {ops}")
print()

#6. Спортивное расписание
a = float(input("Please enter your current results: "))
b = float(input("What is your target?: "))
day = 1
c_perf = a
while a < b:
    a = a * 1.1
    day = day + 1

print (f"You will reach your goal in {day} days and your approximated result will be {a} km")