# def f(x):
#     return x*x
# print(f(5))

# Выбрать из списка четные числа и вывести их, а также квадрат этого числа
# list_1=[1, 2, 3, 5, 8, 15, 23, 38]
# res=list()
# for i in list_1:
#     if i%2==0:
#         res.append((i, i**2))
# print(res)

# В данном коде можно убрать из начала кода и заменить функцию  select на map. 
# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# list_1=[1, 2, 3, 5, 8, 15, 23, 38]
# res=select(int, list_1)
# print(res)
# res=where(lambda x: x%2==0, res)
# print(res)
# res=list(select(lambda x: (x, x**2), res))
# print(res)

# s='hgaGDkjh^&%$hgKG'
# while len(s)>0:
#     bukva=s[0]
#     if bukva>='a' and bukva<='z':
#         print(bukva, 'small')
#     elif bukva>='A' and bukva<='Z':
#         print(bukva,'big')
#     elif bukva.isdigit():
#         print(bukva,'digit')
#     else:
#         print(bukva,'znak')
#     s=s[1:]

# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).Если строк меньше двух, выдайте текст ОШИБКА! Размерности таблицы должны быть больше 2!.Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.Между элементами должен быть 1 пробел, в конце строки пробел не нужен.
# def print_operation_table(operation, num_rows = 9, num_columns = 9): 
#     if num_rows <2 or num_columns <2:  
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         for i in range(1, num_rows + 1):
#             lst=[]
#             for j in range(1,num_columns + 1):
#                 lst.append((operation)(i, j))
#             # ls=lst
#             # ls.rjust(16,' ')
#             print(*ls)
        
# print_operation_table(lambda x, y: x * y, 6, 6)

# Задача от преподавателя(см.конец лекции 7)
# values = [0, 2, 10 ,6, 4, 8]
# if len(values) == len(list(filter(lambda x: x % 2 == 0, values))):
# print('same')
# else:
# print('different')

# def same_by(op, x):
# return len(list(filter(op, x))) == len(x)


# if (same_by(lambda x: x % 2 == 0, values)):
# print('same', '👍')
# else:
# print('different', '👎')


       
                

#Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.Фразы отделяются друг от друга пробелами.Стихотворение Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!

#st = 'пара-рама'.split()
# if len(st)>1:
#     ls=[]
#     for i in st:
#         ls.append(len([1 for x in i if x in 'ауоыиэяюёе']))
#     #if len(set(ls))==1:
#     if max(ls)==min(ls):
#         print('Парам пам-пам')
#     else:
#         print('Пам парам')
# else:
#     print('Количество фраз должно быть больше одной!')

# Загрузка справочника из файла, если он существует
