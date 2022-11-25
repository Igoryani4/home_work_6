import crud as cr
import logger as lg
import user_interface as ui



def update_surname():
    lg.logging.info('The user has selected item number 6.1')
    search = ui.input_surname()
    lg.logging.info('User entered: {search}')
    cr.retrive(surname=search)
    user_id = ui.input_id()
    lg.logging.info('User entered: {user_id}')
    new_number = ui.input_new_number_phone()
    lg.logging.info('User entered: {new_number}')
    cr.update(id=user_id, new_number = new_number)




def update_car_number():
    lg.logging.info('The user has selected item number 6.2')
    search = ui.input_car_number()
    lg.logging.info('User entered: {search}')
    cr.retrive(car_number=search)
    user_id = ui.input_id()
    lg.logging.info('User entered: {user_id}')
    new_number = ui.input_new_car_number()
    lg.logging.info('User entered: {new_number}')
    cr.update(id = user_id, new_car_number = new_car_number)

    
def update_phone_number():
    lg.logging.info('The user has selected item number 6.3')
    search = ui.input_phone_number()
    lg.logging.info('User entered: {search}')
    cr.retrive(number = search)
    user_id = ui.input_id()
    lg.logging.info('User entered: {user_id}')
    new_number = ui.input_new_number_phone()
    lg.logging.info('User entered: {new_number}')
    cr.update(id=user_id, new_number=new_number)
    
    

    
