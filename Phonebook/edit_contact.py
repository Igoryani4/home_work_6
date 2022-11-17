from csv_reading import edit_csv
from File_writing import writing_scv


def edit_contact(position):
    
    ph_lst = [i.split(';') for i in edit_csv()]
    
    print('Изменить:\n1. Фамилию\n2. Имя\n3.Телефон\n4.Описание')
    edit_choice = int(input())
    ph_lst[position - 1][edit_choice - 1] = input('Введите новое значение:')
    
writing_scv()

edit_contact(2)