# from modul1 import max1
# #import modul1
# print(max1(10,5))

#Найти пересечения чисел в спиках и вывести их в порядке возрастания
# var1 = '5 4'
# var2 = '5 6 7 8 1 4'
# var3 = '6 7 8 9 4 2' 
# set1 = set(map(int,var2.split()))
# set2 = set(map(int,var3.split()))
# common_elements=(sorted(set1.intersection(set2)))
# print(*common_elements)

# В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, и кусты черники высажены по окружности грядки. Каждый куст черники имеет урожайность, которая соответствует количеству ягод на этом кусте. Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность (количество ягод) i-го куста. В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.

#Пробный
#arr = [5, 9, 6, 4, 10, 2, 7, 3]
#a = list(map(int, input().split()))
# def max_ber(arr):
#     n = len(arr)
#     max_ber = 0
#     for i in range (n):
#         ber=arr[i]+ arr[i-2] + arr[i-1]
#         if ber > max_ber:
#             max_ber = ber
#     return max_ber
# result=max_ber(arr)
# print(result)

#def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)
# list_1=[]
# for i in range(1,10):
#     list_1.append(fib(i))
# print(list_1)     

# Функция принимает одно число и проверяет , является ли оно простым
# n=101
# def number(num, dl=2):
#     if num==2 or dl*dl>num:   
#         return 'yes'
#     elif num % dl==0:
#         return 'no'
#     return number(num,dl+1)
# print(number(n))

#Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.Функция не должна ничего выводить, только возвращать значение.
# a = 6
# b = 5
# #print(sum(a, b))
# def sum(a,b):
#     if a==0:
#         return b
#     elif b==0:
#         return a
#     else:
#         return sum(a-1,b+1)
# print(sum(a,b))

# Задача No37. Решение в группах.Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке. Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода). Input: 2 -> 3 4 Output: 4 3

# def revers (number):
#     if number==0:
#         return '+'
#     num=input('Введите число:')
#     return revers(number-1)+num
# n=int(input())
# print(revers(n))

# def print_reverse_seq(seq):
#     if not seq:
#         return " "
#     else:
#         print(seq[-1], end='')
#         print_reverse_seq(seq[:-1])
# n = int(input())
# seq = list(map(int, input().split()))
# print_reverse_seq(seq)


# # определить слово палиндром с помощью рекурсии
# a= str(1234322)
# def f(a):
#     if len(a)<2:
#         return True
#     elif a[0]==a[-1]:
#         return f(a[1:-1])
#     else:return False
# print(f(a))

# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии. (первая программа выполненная самостоятельно)
# a=3
# b=5
# def f(a,b):
#     if b==0:
#         return 1
#     elif a==0:
#         return False
#     #else:
#     return (a**b)
# print (f(a, b))

# С использованием функции POW
#    
# Найти слово палиндром
# def palindrom (str):
#     if len (str)<=1:
#         return True
#     if str[0]!=str[-1]:
#         return False
#     return palindrom (str[1:-1])
# print(palindrom('шалаш'))

# def greet(name):
#     print(f"Привет, {name}!")

# greet("Анна")

#Напишите функцию calculate_average, которая принимает список чисел в качестве аргумента и возвращает среднее арифметическое этих чисел:
# def calculate_avarage (numbers):
#     if len(numbers)==0:
#         return 0
#     total= sum(numbers)
#     avarage=total/len(numbers)
#     return avarage
# numbers =[21, 43, 29,54, 12]
# avg = calculate_avarage(numbers)
# print (avg)

#Напишите функцию print_square, которая принимает число в качестве аргумента и выводит на экран его квадрат, но ничего не возвращает:

# def print_square (number):
#     square = number**2
#     print(f'Квадрат числа {number} равен {square}')
# print_square(12)

#Вы также можете создать функцию, которая принимает как неименованные, так и именованные параметры:
# def comb_func(arg1, arg2, *args, **kwargs):
#     print(f"arg1: {arg1}")
#     print(f"arg2: {arg2}")
#     print(f"Дополнительные аргументы: {args}")
#     print(f"Именованные аргументы: {kwargs}")
#comb_func(1, 2, 3, 4, 5, name="Анна", age=30)

#Вы также можете создать функцию, которая принимает как  именованные параметры:
# def info_user(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# info_user(name="Анна", age=30, city="Москва")

#Напишите функцию сумма_двух_чисел, которая принимает два аргумента и возвращает их сумму.
# def sum_two_number(a, b):
#     return a+b
# print(sum_two_number(5, 6))

#Напишите функцию сумма_произвольных_чисел, которая принимает произвольное количество чисел и возвращает их сумму
# def sum_number(*args):
#     return sum(args)
# result= sum_number(3, 1, 2)
# print(f'Сумма значений:', result)

#Напишите функцию приветствие, которая принимает имя и возраст, где возраст является необязательным аргументом со значением по умолчанию.
# def privetsvie (name, age=25):
#     print(f' Привет: {name}, тебе {age} лет')
# privetsvie ('Роман', 'больше 40')