# import sys
# data = [42, 73.0, 'Hello world!', True, 42, 'Hello world!', 256, 2 ** 8, 1, 'Привет, мир!']
# for n, item in enumerate(data, 1):
#     print(n, item)
#     check_int = 'Число является целым' if isinstance (item, int) else 'Число не является целым'
#     check_str = 'Это строка' if isinstance (item, str) else ''
#     print (f'{n}. Объект {item}\nАдрес:{id(item)}\tРазмер: {sys.getsizeof(item)}\t' f'Хэш: {hash(item)} {check_int}{check_str}')

### Задачи по семинару №2
# Задание №3
# Напишите программу, которая получает целое число и возвращает 
# его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего 
# результата, а не для решения.
# Дополнительно:Попробуйте избежать дублирования кода 
# в преобразованиях к разным системам счисления
# Избегайте магических чисел Добавьте аннотацию типов где это возможно

# BIN=2
# OCT=8

# num: int=int(input('Введите число:'))
# for div in BIN, OCT:
#     test_num: int = num
#     res: str = ''
#     while test_num:
#         cur_num= test_num % BIN
#         res= str(cur_num) + res
#         test_num//= BIN
#     print(f'для {BIN} {res=}')

# Задание №4 Напишите программу, которая вычисляет площадь 
# круга и длину окружности по введённому диаметру. 
# Диаметр не превышает 1000 у.е. Точность вычислений должна составлять 
# не менее 42 знаков после запятой.

# import math 
# import decimal

# decimal.getcontext().prec = 50
# PI = decimal.Decimal(math.pi)

# d= decimal.Decimal (input('Введите диаметр: '))
# s= PI * (d/2)**2
# l= PI * d
# print(f'{s=}')
# print(f'{l=}')
# import math
# import decimal
# decimal.getcontext().prec = 50
# PI = decimal.Decimal(math.pi)
# d = decimal.Decimal(input('Введите диаметр: '))
# while d > 1000:
#     print('Введено число вне диапазона, больше 1000')
#     d = decimal.Decimal(input('Введите диаметр: '))
# decimal.Decimal
# s = PI * (d/2) ** 2
# l = PI * d

# Задание №5 Напишите программу, которая решает квадратные уравнения даже если 
# дискриминант отрицательный. Используйте комплексные числа 
# для извлечения квадратного корня.

# a= float (input('Введите коэффециент a: '))
# b= float (input('Введите коэффециент b: '))
# c= float (input('Введите коэффециент c: '))
# d= b ** 2 - 4 * a * c
# if d>0:
#     x1 = (-b + d**0.5)/(2*a)
#     x2 = (-b - d**0.5)/(2*a)
#     res=f'У уравнения 2 корня:{x1=} {x2=}'
# elif d==0:
#     x = -b/ (2*a)
#     res = f'У уравнения один корень:{x=}'
# else:
#     d=complex(d,0)
#     print(d)
#     x1 = (-b + d**0.5)/(2*a)
#     x2 = (-b - d**0.5)/(2*a)
#     res=f'У уравнения 2 корня:{x1=} {x2=}'
#     print(res)

# Задание №6 Напишите программу банкомат. 
# Начальная сумма равна нулю Допустимые действия: пополнить, снять, выйти. Сумма пополнения и снятия кратны 50 у.е. Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е. После каждой третей операции пополнения или снятия начисляются проценты - 3%. Нельзя снять больше, чем на счёте При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной. Любое действие выводит сумму денег

# import decimal

# CMD_WITHDRAW = "с"
# CMD_DEPOSIT = "п"
# CMD_EXIT = "в"
# MULTIPLICITY = 50
# NUMBER_OPERATION = 3
# PRECENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
# RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
# RICHNESS_SUM = decimal.Decimal(5_000_000)
# MIN_REMOVAL = decimal.Decimal(30)
# MAX_REMOVAL = decimal.Decimal(600)
# PRECENT_BONUS = decimal.Decimal(3) / decimal.Decimal(100)

# balance = decimal.Decimal(60000000)
# count = 0

# while True:
#     action = input(f"Пополнить - '{CMD_DEPOSIT}', снять - '{CMD_WITHDRAW}', выйти - '{CMD_EXIT}' ")
#     if action == CMD_EXIT:
#         print(f"Заберите карту. баланс:{balance}у.е")
#         break
#     if balance > RICHNESS_SUM:
#         percent = balance * RICHNESS_PERCENT
#         balance -= percent
#         print(f"Вычтен налог на богатство {RICHNESS_PERCENT * 100}%. "
#               f"Сумма процента - {percent}. Баланс карты - {balance}")

#     if action in (CMD_DEPOSIT, CMD_WITHDRAW):
#         amount = 1
#         while amount % MULTIPLICITY != 0:
#             amount = decimal.Decimal(input(f"Введите сумму кратнную {MULTIPLICITY}: "))

#         if action == CMD_DEPOSIT:
#             count += 1
#             balance+=amount
#             print(f"Пополнение карты на {amount}. Баланс карты: {balance}")
#         elif action == CMD_WITHDRAW:
#             percent=amount*PRECENT_REMOVAL
#             percent= MIN_REMOVAL if percent<MIN_REMOVAL  else MAX_REMOVAL if percent>MAX_REMOVAL else percent
#             sub=amount+percent
#             if balance>sub:
#                 balance-=sub
#                 count+=1
#                 print(f"Снятие с карты {amount}у.е. Сумма процента за снятие {percent}. "
#                       f"Баланс карты {balance}")
#             else:
#                 print(f"Недостаточно средств. Сумма снятия {amount}. Сумма процента за снятие {percent}."
#                       f"Баланс карты {balance}")
#     if count%NUMBER_OPERATION==0:
#         bonus = balance * PRECENT_BONUS
#         balance+=bonus
#         print(f"Начислен бонус: {bonus} за каждую {NUMBER_OPERATION}. Баланс карты {balance}")


# Задание №1
#  Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные (без повтора) элементы исходного списка. Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.

# data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]
# print(f'Новое множество:{list(set(data))}')

# new_list=[]
# for item in data:
#     if item not in new_list:
#         new_list.append(item)
# print(new_list)

# new_list_1 = sorted(data)
# for i in range(len(new_list_1)-1,0,-1):
#     if new_list_1[i]==new_list_1[i-1]:
#         del new_list_1[i]
# print(new_list_1)

# Задание №2 Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже: Целое положительное число. Вещественное положительное или отрицательное число. Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква. Строку в верхнем регистре в остальных случаях

# data = input('Введите данные: ')
# if data.isdigit():
#     result = int(data)
# elif data.replace(".","").replace("-","").isdigit()\
#     and data.count('.') < 2 and "-" not in data[1:] :
#     result = float(data)
# elif not data.islower():
#     result = data.lower()
# else:
#     result = data.upper()
# print(f'{result= }')

# Задание №3
# Создайте вручную кортеж содержащий элементы разных типов. 
# Получите из него словарь списков, где:ключ — тип элемента,
# значение — список элементов данного типа.

data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)
result = {}

for item in data:
    item_type = type(item)
    if item_type not in result:
        result[item_type] = [item]
    else:
        result[item_type].append(item)
print(result)

#2
data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)

result = {}

for item in data:
    item_type = type(item)
    if item_type not in result:
        result[item_type] = [el for el in data if type(el) == item_type]

print(result)
#3
data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)

result = {}

for item in data:
    key = result.setdefault(type(item), [])
    key.append(item)
print(result)