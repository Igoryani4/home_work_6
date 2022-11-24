import csv
import os.path
import logger as lg


db_file_name = ''
db = []
global_id = 0  # id для добавления пользователей


def init_data_base(file_name='db.csv'):
    global global_id
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if(row[0] != 'ID'):
                    db.append(row)
                    if(int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(db_file_name, 'w', newline='').close()


def create(name='', surname='', number='', email='', car_number='', car_model=''):
    global global_id
    global db
    global db_file_name
    if(name == ''):
        print(f'Внимание это поле не может быть пустым')
        return
    if(surname == ''):
        print("ALARM NO SURNAME SPECIFIED!!!!!1111")
        return
    if(number == ''):
        print("ALARM NO TELEPHONE NUMBER SPECIFIED!!!!!1111")
        return
    if(email == ''):
        print("ALARM NO EMAIL SPECIFIED!!!!!1111")
        return
    if(car_number == ''):
        print("ALARM NO EMAIL SPECIFIED!!!!!1111")
        return
    if(car_model == ''):
        print("ALARM NO EMAIL SPECIFIED!!!!!1111")
        return

    for row in db:
        if(row[1] == name.title() and row[2] == surname.title() and row[3] == number and row[4] == email.lower()):
            print("already exist")
            return

    global_id += 1
    new_row = [str(global_id), name.title(),
               surname.title(), number, email.lower(), car_number, car_model]
    db.append(new_row)
    with open(db_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


# поиск (если нужно выгрузить все: result = retrive())
def retrive(id='', name='', surname='', number='', email=''):
    global global_id
    global db
    global db_file_name
    count = 0
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if(name != '' and row[1] != name.title()):
            continue
        if(surname != '' and row[2] != surname.title()):
            continue
        if(number != '' and row[3] != number):
            continue
        if(email != '' and row[3] != email.lower()):
            continue
        count += 1
        print(f'{row[0]} \t{row[1]} \t{row[2]} \t{row[3]} \t{row[4]} \t{row[5]} \t{row[6]}')
    if count == 0:
        return f'Контакты не найдены'
    # else:
    #     return for i in range(le)
    #     # return (* result)


def update(id='', new_name='', new_surname='', new_number='', new_email=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for update')
        return
    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            if(row[0] == id):
                if(new_name != ''):
                    row[1] = new_name.title()

                if(new_surname != ''):
                    row[2] = new_surname.title()

                if(new_number != ''):
                    row[3] = new_number

                if(new_email != ''):
                    row[3] = new_email.lower()

            writer.writerow(row)


def delete(id=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for delete')
        return

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break

    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)


def get_token():
    file = open('token.csv', 'r')
    for i in file:
        token = i
    file.close()
    return token

