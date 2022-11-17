from File_writing import writing_scv
from File_writing import writing_txt
from csv_reading import read_csv
from edit_contact import edit_contact


def get_info():
    info = []
    
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = ''
    valid =False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info


def menu():

    print("Привет, я твой телефонный справочник, я умею:")
    print('1. Создать контакт\n2. Редактировать контакт\n3. Удалить контакт\n4. Вывести список контактов')
    choice = int(input())
    if choice == 1:
        get_info()
        writing_scv ()
        writing_txt ()
    elif choice == 2:
        edit_contact(choice)
        writing_scv ()
        writing_txt ()
    elif choice == 3:
        del_contact()
        writing_scv ()
        writing_txt ()
    else:
        read_csv






