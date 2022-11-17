


# def read_book():
#     while open ('Phonebook.csv', 'r'):
#         phone_list.writeline()

import csv

# FILENAME = "Phonebook.csv"
 
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.reader(file)
#     for row in reader():
#         print(row)
def read_csv():
    filename = "Phonebook.csv"
    with open(filename, encoding="utf8") as file:
        text = file.readlines()
        phone = [text[i].replace(';', ' ') for i in range(len(text))]
    
    print(* phone)
    

def read_txt():
    filename = "Phonebook.txt"
    with open(filename, encoding="utf8") as file:
        text = file.readlines()
        phone = [text[i].replace(';', ' ') for i in range(len(text))]
    
    print(* phone)

def edit_csv():
    filename = "Phonebook.csv"
    with open(filename, encoding="utf8") as file:
        text = file.readlines()
        return text