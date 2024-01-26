#Домашка  "Телефонный справочник"
try:
    with open('Phonebook.txt', 'r') as file:
        phonebook = 'Phonebook.txt'
        json.load(file)
except FileNotFoundError:
    phonebook = {}

def display_phonebook():
    print("Телефонный справочник:")
    for name, last_name, number in phonebook.items():
        print(f"{name}:{last_name}:{number}")

def find_contact_by_name(name):
    if name in phonebook:
        print(f"Найден абонент: {name} - {last_name} - {phonebook[name]}")
    else:
        print(f"Абонент с именем {name} не найден")

def find_contact_by_number(number):
    for name, num in phonebook.items():
        if num == number:
            print(f"Найден абонент: {name} -{last_name}- {number}")
            return
    print(f"Абонент с номером {number} не найден")

def add_contact(name,last_name, number):
    phonebook[name, last_name] = number
    print(f"Абонент {name}-{ last_name} успешно добавлен в справочник")

def save_phonebook():
    with open('phonebook.json', 'w') as file:
        json.dump(phonebook, file)
    print("Справочник сохранен в файле Phonebook.txt")

# Основной цикл программы
while True:
    print("\nВыберите необходимое действие:\n")
    print("1. Отобразить весь справочник")
    print("2. Найти абонента по фамилии")
    print("3. Найти абонента по номеру телефона")
    print("4. Добавить абонента в справочник")
    print("5. Сохранить справочник в текстовом формате")
    print("6. Закончить работу")

    choice = input("Выберите действие: ")
    if choice == "1":
        display_phonebook()
    elif choice == "2":
        name = input("Введите фамилию абонента: ")
        find_contact_by_name(name, last_name)
    elif choice == "3":
        number = input("Введите номер телефона: ")
        find_contact_by_number(number)
    elif choice == "4":
        name = input("Введите имя абонента: ")
        last_name = input("Введите фамилию абонента: ")
        number = input("Введите номер телефона: 900-")
        add_contact(name, last_name, number)
    elif choice == "5":
        save_phonebook()
    elif choice == "6":
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")