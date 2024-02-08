# a=input('Введите слово:')
# print (type(a) , id(a), hash (a))
# # print ( id(a))
# # print (hash (a))

# import sys
# data = [42, 73.0, 'Hello world!', True, 42, 'Hello world!', 256, 2 ** 8, 1, 'Привет, мир!']
# for n, item in enumerate(data, 1):
#     print(n, item)
#     check_int = 'Число является целым' if isinstance (item, int) else 'Число не является целым'
#     check_str = 'Это строка' if isinstance (item, str) else ''
#     print (f'{n}. Объект {item}\nАдрес:{id(item)}\tРазмер: {sys.getsizeof(item)}\t' f'Хэш: {hash(item)} {check_int}{check_str}')

# Задание №3
# Напишите программextend, которая полextendчает целое число и возвращает 
# его двоичное, восьмеричное строковое представление.
# Фextendнкции bin и oct использextendйте для проверки своего 
# резextendльтата, а не для решения.
# Дополнительно:Попробextendйте избежать дextendблирования кода 
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

# res=input('Введите текст: ')
# if int(res, base=36):
#     b = bin(res)
#     o = oct(res)
#     x = hex(res)  
# print(b, o, x)

# Лекция №3(Коллекции)

# my_list=[2, 4, 6, 8, 10]
# print(my_list[-1])

# Метод .append()
# a=42
# b='Hello world!'
# c=[1, 3, 5, 7]
# my_list=[None]
# my_list.append(a)
# print(my_list)
# my_list.append(b)
# print(my_list)
# my_list.append(c)
# print(my_list)

# Метод .extend()
# a=42
# b='Hello world!'
# c=[1, 3, 5, 7] 
# my_list=[None]
# # my_list.extend(a)
# print(my_list)
# my_list.extend(b)
# print(my_list)
# my_list.extend(c)
# print(my_list)

# Метод .pop()
# my_list=[2, 4, 6, 8, 10]
# spam = my_list.pop()
# print(spam, my_list)
# eggs = my_list.pop (2)
# print(eggs, my_list)

# Метод .count()
# my_list=[2, 4, 2, 10, 8, 6, 8, 10, 8, 8]
# a = my_list.count(8)# ищет количнество повторений числа 8 в списке 
# print(a)

# Метод .index()
# my_list=[2, 4, 2, 10, 8, 6, 8, 10, 4, 8, 8]
# spam = my_list.index(4) #ищет первое вхождение цифры 4 в списке
# print(spam)
# eggs = my_list.index(4, spam +1, 90) # повторно ищем цифру 4,начиная со 2го элемента до ячейки с номером 90(если списсок меньше, то до конца списка)
# print(eggs)

# Метод .insert()
# my_list=[2, 4, 2, 10, 8, 6, 8, 10, 4, 8, 8]
# my_list.insert(2, 555) # вставит число 555 на 2й индекс. 2 вариант написания: my_list[2]= 155
# print(my_list)
# my_list.insert(42, 173) # вставит число 173 в конец списка. 
# print(my_list)

# Метод .remove()
# my_list=[2, 4, 2, 10, 8, 6, 8, 10, 4, 8, 8]
# my_list.remove(10) # удалит первое найденное число 10
# print(my_list)

# Функция .sorted()
# my_list=[2, 4, 2, 10, 8, 6, 8, 10, 4, 8, 8]
# sort_list = sorted(my_list) # отсортирует список по возрастанию слева-направо
# print(my_list, sort_list, sep='\n')
# rev_list = sorted(my_list, reverse=True) # отсортирует список по убыванию. По умолчанию стоит False. Для сортировки по убыванию нужно указать True
# print(my_list, rev_list, sep='\n')

# Функция .copy()
# my_list=[2, 4, 2, 10, 8, 6, 8, 10, 4, 8, 8]
# new_list = my_list.copy() # копирует список my_list в новый список new_list, не меняя содержимое старого. Если не создать копии, поменяются об списка.
# print(my_list, new_list, sep='\n')

#Функция .deepcopy()
# matrix=[[2, 4, 2] [10, 8, 6] [8, 10, 4]]
# new_m = matrix.copy() # Создаент поверхностную копию списка matrix. 
# print(matrix, new_m, sep='\n') # Если не создать копии, поменяются об списка.
# matrix[0][1]=555 # заменит 4 в первом вложенном списке и заменит ее в созданном new-m 
# print(matrix, new_m, sep='\n')

# matrix=[[2, 4, 2] [10, 8, 6] [8, 10, 4]]
# new_m = copy.deepcopy(matrix) # Создаент более глубокую копию списка matrix. 
# print(matrix, new_m, sep='\n') # Если не создать копии, поменяются об списка.
# matrix[0][1]=555 # заменит 4 в первом вложенном списке matrix и не заменит ее в новом созданном new-m 
# print(matrix, new_m, sep='\n')

# my_list=[2, 4, 2, 10, 8, 6, 8, 10, 4, 8, 8]
# print(my_list.extend([314,42])) # метод extend добавляет значения в список, но ничего не выводит. Поэтому выведится значение None.  
# print (my_list.sort(reverse=False)) # метод sotr отсортирует список на месте и выведет None. Список будет отсортирован слева-направо(т.к стоит False), 42 и 314 будут в конце списка.
# print (my_list)

### Форматирование
# Метод .format()
# name = 'Alex'
# age = 12
# text = 'Меня зовут {}  и мне {} лет'.format (name, age)
# print(text) 

# Метод .f-строк{}
# name = 'Alex'
# age = 12
# text = f'Меня зовут {name}  и мне {age} лет'
# print(text) 

#print(f'{{ Фигурные скобки}} и {{name}}')

# Другие виды форматирования
# pi= 3.1415
# print(f'Число Пи с точностью два знака: {pi:.2f}') #  выведит  в значении 2 числа после запятой. f - означает float.

# data = [2453, 1746579317, 548723, 4566, 346219, 1651]
# for item in data:
#     print(f'{item:>10}') # выводит итерируемые объекты с выравниванием в 10 символов вправо. (^ - выравниваем по центру, < - выравниваем влево)

# num = 2 * pi * data [1]
# print(f'{num = :_}') # разбиваем полученное число символом _ по 3 знака.

### Словари
## Варианты создания:
# a = {'one': 42, 'two': 3.14, 'ten': 'Hello world'}
# b = dict (one=42, two=3.14, ten='Hello world') # при создании словаря ключи будут переведены в строки
# c = dict ([('one',42), ('two',3.14), ('ten','Hello world')]) # в виде списка с вложенными кортежами
# print (a==b==c)

# Добавление значения с словарь

# my_dict={'one': 1, 'two': 2, 'three':3}
# #x=10
# my_dict['ten']=10
# print(my_dict)
 