#Программа про работу с телефонным справочником.
def work_with_phonebook():
    print('Телефонный справочник:')
    stop='No'
    choice=show_menu(stop)
    phone_book=read_txt('Phonebook.txt')
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    while choice >=7:
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Введите Фамилию:')
            print(find_by_lastname(Phone_book,last_name))
        elif choice==3:
            number=input('Введите номер телефона:900-')
            print(change_number(Phone_book, number))
        elif choice==4:
            NewLastName=input('Введите фамилию:')
            NewName=input('Введите имя:')
            NewPhone=input('Введите номер: 900-')
            print(add_by_lastname(Phone_book,Newlastname, NewName, NewPhone))
        elif choice == 5:
            save_phonebook('Phonebook.txt')
        elif choice == 6:
            break
        else:
            print("Некорректный ввод. Попробуйте снова!")
        choice=show_menu(stop)
def show_menu(stop): 
    print("\n Выберите необходимое действие:\n"
        "1. Отобразить весь справочник\n"
        "2. Найти абонента по фамилии\n"
        "3. Найти абонента по номеру телефона\n"
        "4. Добавить абонента в справочник\n"
        "5. Сохранить справочник в текстовом формате\n"
        "6. Закончить работу")
def read_txt(Phonebook):
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open('Phonebook.txt','r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.rstrip ('\n').split(',')))
            phone_book.append(record)
    return phone_book
def print_result(phone_book):
    return phone_book
    choice=show_menu()

    while True:
        choice=show_menu()        
#filename= 'Phonebook.txt'        
phone_book=read_txt('Phonebook.txt')       
def write_txt(filename , Phone_book):
    with open('Phonebook.txt','w',encoding='utf-8') as phout:
        for i in range(len(Phone_book)):
            s=''
            for v in Phone_book[i].values():
                s+=v+','
    phout.write(f'{s[:-1]}\n')

work_with_phonebook()

