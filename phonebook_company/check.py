import crud as cr
import logger as lg
import user_interface as ui
import searh as sh
import create


def сhecking_the_number(arg):
    while arg.isdigit() != True:
        lg.logging.info('User entered an invalid menu value: {arg}')
        arg = ui.message()
        lg.logging.info('User entered: {arg}')
    return int(arg)

def all_contact():
    lg.logging.info('The user has selected item number 1')
    print(cr.retrive())
    
    
def check_surname():
    lg.logging.info('The user has selected item number 2')
    search = ui.input_surname()
    lg.logging.info('User entered: {search}')
    print(cr.retrive(surname = search))
    
def check_car_number():
    lg.logging.info('The user has selected item number 3')
    search = ui.input_car_number()
    lg.logging.info('User entered: {search}')
    print(cr.retrive(car_number = search))
    
def check_phone_number():
    lg.logging.info('The user has selected item number 4')
    search = ui.input_phone_number()
    lg.logging.info('User entered: {search}')
    print(cr.retrive(number = search))
  
 
def check_menu(n):
    if n == 1:
        all_contact()
        
    elif n == 2:
        check_surname()
        
    elif n == 3:
        check_car_number()
        
    elif n == 4:
        check_phone_number()
        
    elif n == 5:
        create.new_contact()
        
    elif n == 6:
            lg.logging.info('The user has selected item number 6')
            ui.change_contact()
            
            if change == 1:
                sh.update_surname()
                
            elif change == 2:
                sh.update_car_number()

            elif change == 3:
                sh.update_phone_number()
                

            else:
                lg.logging.info('User entered an invalid menu value')
                chek_list = [1,2,3]
                while change not in chek_list:
                    change = ui.right_input()
                    lg.logging.info('User entered: {change}')
                if change == 1:
                        sh.update_surname()
                
                elif change == 2:
                        sh.update_car_number()

                elif change == 3:
                        sh.update_phone_number()
                

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
            print('Всего доброго!!!, Спасибо что пользуетесь нашей базой данных')
            break

        else:
            lg.logging.info('User entered an invalid menu value: {n}')
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

  
  
