def import_data_txt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
    return data
filename = 'phonebook.txt'
data_txt = import_data_txt(filename.split())
print(data_txt)
def display_phonebook():
    print("Телефонный справочник:")
    for last_name,name, number in phonebook.items():
        print(f"{last_name}: {name}: {number}")
def find_contact_by_last_name(last_name):
    if last_name in phonebook:
        print(f"Найден абонент: {phonebook[last_name]}: {phonebook[name]}: {phonebook[number]}")
    else:
        print(f"Абонент с фамилией {last_name} не найден")
def find_contact_by_number(number):
    for last_name, name, num in phonebook.items():
        if num == number:
            print(f"Найден абонент: {last_name} -{name} - {number}")
            return
    print(f"Абонент с номером {number} не найден")

def add_contact(last_name, name, number):
    phonebook[last_name, name] = number
    print(f"Абонент {last_name}: {name} успешно добавлен в справочник")
def save_phonebook():
    with open('phonebook.txt', 'w') as file:
        for last_name, name, number in phonebook.items():
            file.write(f" {last_name}: {name}: {number}\n")
    print("Справочник сохранен в файле phonebook.txt")
# Основной цикл программы
while True:
    print("\nМеню:")
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
        find_contact_by_last_name(last_name)
    elif choice == "3":
        number = input("Введите номер телефона: ")
        find_contact_by_number(number)
    elif choice == "4":
        last_name = input('Введите фамилию абонента: ')
        name = input("Введите имя абонента: ")
        number = input("Введите номер телефона: ")
        add_contact(last-last_name, name, number)
    elif choice == "5":
        save_phonebook()
    elif choice == "6":
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")