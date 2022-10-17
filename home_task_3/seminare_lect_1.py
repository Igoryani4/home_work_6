#Работа в группе на семинарах
# def findTwice():
#     for i in list:
#         if i.find(numstr):
#             return True

# len_list = open('file.txt', 'r')
# list=[]
# for l in len_list.readlines():
#     list = (l.split(' '))
# len_list.close()
# print(list)
# num= 95
# numstr= str(num)

# print(findTwice())


from datetime import datetime
import time

from datetime import datetime

def get_rand_int(num):
    time = datetime.now()
    rng = time.microsecond
    return rng % num

print('Случайные числа: ')
print(get_rand_int(100))




def check_brackets(brc):
    stack = []
    brc_open = {'(': ')', '[': ']', '{': '}'}

    for i in range(len(brc)):
        if brc[i] in brc_open.keys():
            stack.append(brc[i])
        elif brc[i] in brc_open.values():
            if len(stack)>0:
                b = stack.pop()
                if brc_open[b] != brc[i]:
                    return i
        else:
            return i
    if len(stack) == 0:
        return 0
    else:
        return len(brc)

print(check_brackets('([11]{{[33]}})'))
s = '([1+1]{{[3**5]}))-3})'
print(s)
pos = check_brackets(s)
if pos > 0:
    st = ' '*pos
print(f'{st}^')