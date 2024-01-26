# # a=5
# # b=2
# def max1(a,b):
#     if a>b:
#         return a
#     return b

# Про число Фибоначи
# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)
# list_1=[]
# for i in range(1,10):
#     list_1.append(fib(i))
# print(list_1)    

#Быстрая сортировка
# def quick_sort(array):
#     if len(array)<=1:
#         return array
#     else:
#         pivot=array[0]
#     less= [i for i in array[1:] if i<=pivot]  
#     greater= [i for i in array[1:] if i>pivot]   
#     return quick_sort(less)+[pivot]+quick_sort(greater)
# print(quick_sort([14,5,6,8,9,36,57,2]))

# Функции
# def say():
#     print('привет')
#     print('здорово')
#     print('старайся больше')
# def square(x):
#     print('Квадрат числа',x,'=',x**2)
# for i in range(1,11):
#     square(i)
# def multyply(a,b):
#     print(a*b)
# multyply(3,5)
# multyply(15,15)
# say()
# print('pause') 
# say()
    
# def even(a):
#     if a%2==0:  
#         print(a,'четное')
#     else:
#         print(a,'нечетное')

# Факториал числа
# def factorial(n):
#         pr=1
#         for i in range(2, n+1):
#              pr=pr*i 
#         print(pr)  
# factorial(5) 


# if 5>9:
#      def primer():
#           print('hello')
# else:
#      def primer():
#           print('HELLO')
# primer()  
              
# for i in range(1,20):
#     even(i)
#even(9)

# Рисует квадраты красного и синего цвета        
# import turtle
# def move(a):
#     turtle.forward(a)  
#     turtle.left(90)
# def drawSquare(a):
#     for i in range(4):
#         move(a)
# def drawSquareColor(a,color): 
#     turtle.color(color)
#     turtle.begin_fill()
#     drawSquare(a)
#     turtle.end_fill()             
# turtle.speed(1)
# drawSquareColor(60, 'red')

# turtle.goto(150,150)
# drawSquareColor(120, 'blue')

# Хотел нарисовать прямоугольники
# import turtle
# def move(a,b):
#     turtle.forward(a)
#     turtle.forward(b)  
#     turtle.left(90)
# def drawSquare(a,b):
#     for i in range(4):
#         move(a,b)
# def drawSquareColor(a,b,color): 
#     turtle.color(color)
#     turtle.begin_fill()
#     drawSquare(a, b)
#     turtle.end_fill()             
# turtle.speed(2)
# drawSquareColor(30,10,'red')
# turtle.goto(100,110)
# drawSquareColor(100,10,'blue')

# Ищет факториалы деления
# def factorial(x):
#     pr=1
#     for i in range(2, x+1):
#         pr=pr*i
#     return pr
# def sochet(n, k):
#     return factorial(n)/(factorial(k)*factorial(n-k))
# print(sochet(10,3))

# Вывод площади и периметра

# def sqAndPer(a, b):
#     return a*b, 2*(a+b)
# square, perimetr=sqAndPer(2,4)
# print(square, perimetr)

# Вывод площади и периметра списком 
# def sqAndPer(a, b):
#     mas=[] 
#     mas.append(a*b)
#     mas.append(2*(a+b))
#     return mas
# print(sqAndPer(2,4))

# print(5*6, round(497/12, 3))
# print(18**0.5)

# задача про переворот монет орлом и решкой
# coins = [0, 1, 0, 1, 1, 0, 0, 0, 1]
# n=0
# n1=0
# for i in coins:
#    if i==0:
#     n+= +1
#    else:
#     n1+= +1
# if n>n1:
#      print(n1)
# else:
#      print(n)     

# coins = [0, 1, 0, 1, 1, 0]
# heads = 0 
# tails = 0 
# for i in range(coins): 
#     if i== 0: 
#         heads += 1 
#     else: 
#         tails += 1 
# print(min(heads, tails))

# #Задача про повторяющееся число в массиве
# list_1 = [1, 2, 3, 4, 5, 1, 1, 1]
# k = 1
# count_k=0
# for i in list_1:
#     if i==k:
#         count_k+=1
# print(count_k)

#Задача про самый близкий по значению элемент к заданному числу К
# list_1 = [1, 2, 3, 4, 5]
# k = 7
# for i in range(len(list_1)):
#     if i < k:
#         nearest_num=-k
#     else:
#         nearest_num = nearest_num + 0
#     if i >= k and i-k<=nearest_num-k:
#         nearest_num=i
#     elif i <= k and nearest_num-k<=i-k:
#         nearest_num=i
# print(nearest_num)   

# list_1 = [1, 2, 3, 6, 7]
# k = 5
# for i in range(len(list_1)):
#     if list_1[i] < k:
#         nearest_num=-k
#     else:
#         nearest_num = nearest_num + 0
#     if list_1[i] >= k and list_1[i]-k<=nearest_num-k:
#         nearest_num=list_1[i]
#     elif list_1[i] <= k and nearest_num-k<=list_1[i]-k:
#         nearest_num=list_1[i]
# print(nearest_num)  

# def closest(lst, K):
#     return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
# #Driver code
# lst = [3,6,4,5,2,9,4,2,9]
# K = 8
# print(closest(lst, K)) 

# import re 
# def Scrabble(text): 
#     return bool(re.search("[а-яА-Я]", text)) 
# Rus = { 1:"А, В, Е, И, Н, О, Р, С, Т", 2:"Д, К, Л, М, П, У", 3:"Б, Г, Ё, Ь, Я", 4:"Й, Ы", 5:"Ж, З, Х, Ц, Ч", 8:"Ш, Э, Ю", 10:"Ф, Щ, Ъ"} 
# Eng = { 1:"A, E, I, O, U, L, N, S, T, R ", 2:"D, G", 3:"B, C, M, P", 4:"F, H, V, W, Y", 5:"K", 8:"J, X"} 
# text = input("Введите слово: ").upper() 
#     if Scrabble(text): 
#         print(sum([k for i in text for k, v in Rus.items() if i in v])) 
#     else: 
#         print(sum([k for i in text for k, v in Eng.items() if i in v]))


# k = 'ноутбук'
# k = k.upper()
# sum = 0
# word = {1:'AEIOULNSTR-АВЕИНОРСТ', 2: 'DG-ДКЛМПУ', 3:'BCMP-БГЁЬЯ', 4:'FHVWY-ЙЫ', 5:'K-ЖЗХЦЧ', 8:'JX-ШЭЮ', 10:'QZ-ФЩЪ'}
# for i in k:
#     print('Ищем букву:',i, 'в слове:' , k )
#     for j in word:
#         print('ключ:',j,'содержит буквы:', word[j])
#         if i in word[j]:
#             print('найдена буква:' , i, 'в ключе:', j,'в слове:', k)
#             print('получено очков:', sum, '+', j)
#             sum+=j
# print(sum)

# Отслеживание строки и подсчет встречающихся символов"
# str='g l h s a a g l'.split()
# slov={}
# for i in str:
#     if i in slov:
#         print(f'{i}_{slov[i]}', end=' ')
#         #slov[i]+=1
#     else:
#         print(i, end=' ') 
#         #slov[i]=1
#     slov[i]=slov.get(i, 0)+1
# print()
# print(slov.get('r', 'нет такого ключа!'))

# Поиск уникальных значений в предложении
# str='ЭпраП;ораор ара;рап папа нныжжло kka;pbmbnmn исси sewwasw'
# str=str.upper().replace('.',' ').replace(";", ' ').split()
# print(set(str))
# print(len(set(str)))

