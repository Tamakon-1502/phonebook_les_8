# # Задание 1. Генерация списка
#
# number = int(input('Введите число: '))
# list_number = []
# for num in range(1, number + 1):
#     if num % 2 != 0:
#         list_number.append(num)
# print('Список из нечётных чисел от одного до N: ', list_number)
#
#
# # Задание 2. Турнир
#
# list_name = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
# list_name_new = []
# for index in range(0, len(list_name)):
#     if index % 2 == 0:
#         list_name_new.append(list_name[index])
# print('Первый день: ', list_name_new)
#
# # 2 вариант
#
# list_name = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
# new_list_name = []
# for index in range(0, len(list_name), 2):
#     new_list_name.append(list_name[index])
# print('Первый день: ', new_list_name)
#
# #
# # Задание 3. Видеокарты
#
# graphics_cards = int(input('Количество видеокарт: '))
# old_graphics_card_list = []
# new_graphics_card_list = []
#
# for number in range(1, graphics_cards + 1):
#     graphics_card = int(input(f'Видеокарта {number} : '))
#     old_graphics_card_list.append(graphics_card)
#     max_number = max(old_graphics_card_list)
#
# for index in range(len(old_graphics_card_list)):
#     if old_graphics_card_list[index] < max_number:
#         new_graphics_card_list.append(old_graphics_card_list[index])
# print('Старый список видеокарт: ', old_graphics_card_list)
# print('Новый список видеокарт: ', new_graphics_card_list)
#
# # Задание 4. Кино
#
# films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия',
#          'Город грехов', 'Мементо', 'Отступники', 'Деревня']
# films_add = int(input('Сколько фильмов хотите добавить? '))
# list_favorite_film = []
# for film in range(1, films_add + 1):
#     film_name = input('Введите название фильма: ')
#     if film_name in films:
#         list_favorite_film.append(film_name)
#     else:
#         print('Ошибка: фильма', film_name, 'у нас нет :(')
#     new_list_films = ','.join(list_favorite_film)
# print('Ваш список любимых фильмов: ', new_list_films)
#
#
# # Задание 5. Контейнеры
#
# count_containers = int(input('Количество контейнеров: '))
# container_list = []
#
# for container in range(1, count_containers + 1):
#     weight_container = int(input('Введите вес контейнера: '))
#     if weight_container < 200:
#         container_list.append(weight_container)
#     else:
#         print('Вес контейнера должен быть меньше 200 кг')
# new_container = int(input('Введите вес нового контейнера: '))
# index = 0
# while index < len(container_list) and container_list[index] >= new_container:
#      index += 1
# print('Номер, который получит новый контейнер:', index + 1)
#
#
# # Задание 6. Бегущие цифры
#
# numbers = int(input("Введите кол-во элементов: "))
# start_list = []
# finish_list = []
#
# for _ in range(numbers):
#     number = int(input('Введите элемент списка: '))
#     start_list.append(number)
#
# shift = int(input("Сдвиг: "))
#
# for i in range(numbers):
#     new_number = start_list[i - shift]# это действие подобрал методом "подбора",
#     # не понятно почему сдвиг чисел идет вправо
#     finish_list.append(new_number)
#
# print(f"Изначальный список: {start_list}")
# print(f"Сдвинутый список: {finish_list}")
#
# # Вариант решения №2 без ввода данных от пользователя. Без действия shift + 1 не переносил список на одну позицию,
# # а повторно печатает старый. Если знаете почему, поясните, я так и не понял. И при вводе сдвига = 3,
# # выпадает ошибка индекса:
# # new_number = numbers_list[index - shift]
# #                  ~~~~~~~~~~~~^^^^^^^^^^^^^^^
# # IndexError: list index out of range
#
# numbers_list = [1, 4, -3, 0, 10]
# finish_list = []
#
# shift = int(input("Сдвиг: "))
#
# for index in numbers_list:
#     new_number = numbers_list[index - shift]
#     finish_list.append(new_number)
#
# print(f"Изначальный список: {numbers_list}")
# print(f"Сдвинутый список: {finish_list}")
#
#
# # Задание 7. Анализ слова — 2 (палиндром)
#
# word = input('Введите слово: ')
# new_word = word[::-1]
# if word == new_word:
#    print('Слово является палиндромом')
# else:
#     print('Слово не является палиндромом ')
#
#
# # Задание 8. Сортировка. Без функции sorted/min/max и метод sort
#
# start_list = [1, 4, -3, 0, 10]
# sort_list = []
# print('Изначальный список:', start_list)# можно использовать такой вывод,
# #a можно объявить переменную и работать сней,
# # чтобы ссылка на start_list не изменялась.
#
# for i in range(len(start_list)):
#     for curr in range(i, len(start_list)):
#         if start_list[curr] < start_list[i]:
#             start_list[curr], start_list[i] = start_list[i], start_list[curr]
#     sort_list.append(start_list[i])
# print('Отсортированный список:', sort_list)
#
# # Задание 9. Обратный анализ чётных чисел
#
# numbers = list(map(int, input("Введите числа через пробел: ").split()))
# finish_list = []
#
# for number in numbers:
#     if number % 2 == 0:
#         finish_list.append(number)
# print(finish_list)# список из неотсортированных четных чисел
#
# while finish_list:
#     print(finish_list.pop(), end=' ')# Вывод четных чисел в обратном порядке
#
#
#
