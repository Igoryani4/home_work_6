import crud as cr
import logger as lg
import search as sh
import check as ch

print('\nЭто база данных клиентов автосалона')

def chenge_contact():
    print('1. Найти клиента по фамилии.')
    print('2. Найти клиента по гос номеру автомобиля.')
    print('3. Поиск по номеру телефона.')
    return ch.сhecking_the_number(input('Введите номер пункта: '))

def ls_menu():
    while True:
        print('\nМЕНЮ')
        print('1. Показать всех клиентов.')
        print('2. Найти клиента по фамилии.')
        print('3. Найти клиента по номеру автомобиля.')
        print('4. Поиск клиента по номеру телефона.')
        print('5. Создать учетную запись клиента.')
        print('6. Изменить учетную запись клиента.')
        print('7. Удалить учетную запись клиента.')
        print('8. Закрыть программу.\n')
        
        n = ср.сhecking_the_number(input('Выберите пункт меню: '))
        
        check_menu(n)

        

# def find(user_choice(n)):

def message():
    print('\nВы ввели не число.')
    return input('Введите соответствующий пункт меню: ')



def input_name():
    return input('Введите имя: ')

def input_car_number():
    return input('Введите номер автомобиля: ')

def input_surname ():
    return input('Введите фамилию: ')

def input_id ():
    return input('Введите id записи: ')

def input_phone_number():
    return input('Введите номер  телефона: ')

def input_email():
    return input('Введите электронную почту: ')

def input_car_model():
    return input('Введите модель автомобиля: ')

def input_new_number_phone():
    return input('Введите новый номер телефона: ')

def input_new_car_number():
    return input('Введите новый номер автомобиля: ')

def right_input():
    return int(input('Введите ВЕРНЫЙ номер пункта: '))


# я закончил на переводе в отдельные функции поиска и из плиска в меню ЮИ 
