import crud as cr
import logger as lg
import user_interface as ui



def search_surname():
    lg.logging.info('The user has selected item number 6.1')
    search = input('Введите фамилию: ')
    lg.logging.info('User entered: {search}')
    cr.retrive(surname=search)
    user_id = input('Введите id записи: ')
    lg.logging.info('User entered: {user_id}')
    new_number = input('Введите новый номер телефона: ')
    lg.logging.info('User entered: {new_number}')
    cr.update(id=user_id, new_number=new_number)




def search_car_number():
    lg.logging.info('The user has selected item number 6.2')
    search = ui.input_car_number()
    lg.logging.info('User entered: {search}')
    cr.retrive(car_number=search)
    user_id = input('Введите id записи: ')
    lg.logging.info('User entered: {user_id}')
    new_number = input('Введите новый номер телефона: ')
    lg.logging.info('User entered: {new_number}')
    cr.update(id=user_id, new_number=new_number)