# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .

# 5) Реализуйте алгоритм перемешивания списка.
#4)#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .

# Реализуйте алгоритм перемешивания списка.

import random
print ('Это программа,  создает список из N элементов, заполненных числами из промежутка [-N, N]. Находит произведение элементов на указанных позициях. Позиции вводятся с клавиатуры')
len_list = int(input('Введите число, длину списка :'))
range_random = int(input('Введите число  диапазон чисел от - до + '))

# list1 = []
# for i in range(len_list):
#     list1.append(random.randint(-range_random, range_random))

list1 = [random.randint(-range_random, range_random) for x in range (len_list)]
    
print(f'Это список случайных чисел: {list1}')

list_find_index = []
len_find_index = int(input('Введите число, сколько ходите умножить индексов: '))
if len_find_index > len_list:
    
    while  len_find_index > len_list or len_find_index < 0 :
        print('Вы ввели количество умножений ВНЕ заданного списка, попробуйте еще: ')
        len_find_index = int(input('Введите правильное число, сколько ходите умножить индексов: '))
    

for i in range (len_find_index):
    index = (int(input(f'Введи {i+1} индекс для умножения: ')))
    if index > len_list - 1 or index <0:
        
        while  index > len_list -1 or index < 0:
            print('Такого индекса в списке нет, попробуйте еще раз')
            index = (int(input('Введи индекс для умножиения: ')))
        
    list_find_index.append(index)
mult = 1        
print (f'Это список индексов для произведения :{list_find_index}')





# Новое решение


mult1 = list(map(lambda num: mult * list1[num], list_find_index))

#Старое решение
# for i in range (len_find_index):
#     mult *= list1[list_find_index[i]]
print (f'Произведение элементов заданных индексов равно :{mult1}')


print('Произвожу произвольное перемешивание списка: ')

random_list = []
num = 0
for i in range (len_list):
    num = (random.randrange(len_list))
    if num not in random_list:
        random_list.append(num)
    else:
        while num in random_list:
            num = (random.randrange(len_list))
        random_list.append(num)
print(f'Это перемешанные индексы списка {random_list}')

list_random_position = [list1[random_list[i]] for i in range(len_list)]

# for i in range (len_list):
#     list_random_position.append(list1[random_list[i]])


print(f'Это список по созданным слуйно индексам {list_random_position}')
