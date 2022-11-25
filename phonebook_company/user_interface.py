import crud as cr
import logger as lg
import search as sh
import check as ch

print('\nЭто база данных клиентов автосалона')


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
        
        n = сhecking_the_number(input('Выберите пункт меню: '))
        
        check_menu(n)

        if n == 1:
            ch.all_contact()

        elif n == 2:
            lg.logging.info('The user has selected item number 2')
            search = input('Введите фамилию: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(surname=search))

        elif n == 3:
            lg.logging.info('The user has selected item number 3')
            search = input('Введите имя: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(name=search))

        elif n == 4:
            lg.logging.info('The user has selected item number 4')
            search = input('Введите номер  телефона: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(number=search))

        elif n == 5:
            lg.logging.info('The user has selected item number 5')
            name = input('Введите имя: ')
            lg.logging.info('User entered: {name}')
            surname = input('Введите фамилию: ')
            lg.logging.info('User entered: {surname}')
            number = input('Введите номер телефона: ')
            lg.logging.info('User entered: {number}')
            email = input('Введите электронную почту: ')
            lg.logging.info('User entered: {email}')
            car_number = input('Введите гос. номер автомобиля: ')
            lg.logging.info('User entered: {car_number}')
            car_model = input('Введите модель автомобиля: ')
            lg.logging.info('User entered: {car_number}')
            cr.create(name, surname, number, email, car_number, car_model)

        elif n == 6:
            lg.logging.info('The user has selected item number 6')
            print('1. Найти клиента по фамилии.')
            print('2. Найти клиента по гос номеру автомобиля.')
            print('3. Поиск по номеру телефона.')
            change = сhecking_the_number(input('Введите номер пункта: '))
            



            if change == 1:
                sh.update_surname()
                

            elif change == 2:
                sh.update_car_number()

            elif change == 3:
                lg.logging.info('The user has selected item number 6.3')
                search = input('Введите номер телефона: ')
                lg.logging.info('User entered: {search}')
                cr.retrive(number=search)
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                lg.logging.info('User entered: {new_number}')
                cr.update(id=user_id, new_number=new_number)

            else:
                lg.logging.info('User entered an invalid menu value')
                chek_list = [1,2,3]
                while change not in chek_list:
                    change = int(input('Введите верный номер пункта: '))
                # change = int(input('Введите верный номер пункта: '))
                

                # print(
                #     '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 7:
            lg.logging.info('The user has selected item number 7')
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            deleting = сhecking_the_number(input('Введите номер пункта: '))

            if deleting == 1:
                lg.logging.info('The user has selected item number 7.1')
                search = input('Введите фамилию: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(surname=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                cr.delete(id=user_id)

            elif deleting == 2:
                lg.logging.info('The user has selected item number 7.2')
                search = input('Введите имя: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(name=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                cr.delete(id=user_id)

            elif deleting == 3:
                lg.logging.info('The user has selected item number 7.3')
                search = input('Введите номер телефона: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(number=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                cr.delete(id=user_id)

            else:
                lg.logging.info('User entered an invalid menu value')
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 8:
            lg.logging.info('End')
            print('Спасибо за работу!')
            break

        else:
            lg.logging.info('User entered an invalid menu value: {n}')
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

# def find(user_choice(n)):



def сhecking_the_number(arg):
    while arg.isdigit() != True:
        lg.logging.info('User entered an invalid menu value: {arg}')
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)

def input_name():
    return input('Введите имя: ')

def input_car_number():
    return input('Введите номер автомобиля: ')

def input_surname ():
    return input('Введите фамилию: ')

def input_id ():
    return input('Введите id записи: ')

def input_new_number_phone():
    return input('Введите новый номер телефона: ')



# я закончил на переводе в отдельные функции поиска и из плиска в меню ЮИ 
