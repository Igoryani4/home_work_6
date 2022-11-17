from os.path  import exists




def creating ():
    file = 'Phonebook.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия;Имя;Номер телефона;Описание\n')

def create_txt ():
    file = 'Phonebook.txt'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия ;Имя; Номер телефона; Описание\n')

def check_file():
    path1 = 'Phonebook.csv'
    path2 = 'Phonebook.txt'
    valid1 = exists(path1)
    valid2 = exists(path2)

    if not valid1:
        creating()
    if not valid2:
        create_txt()