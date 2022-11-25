import crud as cr
import logger as lg
import user_interface as ui

def new_contact():
    lg.logging.info('The user has selected item number 5')
    name = ui.input_name()
    lg.logging.info('User entered: {name}')
    surname = ui.input_surname ()
    lg.logging.info('User entered: {surname}')
    number = ui.input_phone_number()
    lg.logging.info('User entered: {number}')
    email = ui.input_email()
    lg.logging.info('User entered: {email}')
    car_number = ui.input_car_number()
    lg.logging.info('User entered: {car_number}')
    car_model = ui.input_car_model()
    lg.logging.info('User entered: {car_number}')
    cr.create(name, surname, number, email, car_number, car_model)
