print ('Программа переводит целое число из десятичной системы в двоичную или восьмеричную')
try:
    n = int(input('Введите число в десятичной системе: '))
except ValueError:
    print ('Ошибка: неверные входные данные')
    n = 0
try:
    sis = int(input('Введите целевую систему счисления: '))
except ValueError:
    print ('Ошибка: неверные входные данные')
    sis=0
        
n1=0

if (n<0):
    n1=max((-1)*n, n)
else:
    n1=n

def two (x):
    b = ''
    while x > 0:
        b = str(x % 2) + b
        x = x // 2
    return b

def eight (y):
    b = ''
    while y > 0:
        b = str(y % 8) + b
        y = y // 8
    return b

if (n>0):
    if (sis == 2):
        print (two(n1))
    elif (sis == 8):
        print (eight(n1))
    else:
        print ('Входные данные не удовлетворяют условию!')
elif (n==0):
    if (sis == 2) or (sis == 8):
        print (0)
    else:
        print ('Входные данные не удовлетворяют условию!')
elif (n<0):
    if (sis == 2):
        print ('-' + two(n1))
    elif (sis == 8):
        print ('-' + eight(n1))
    else:
        print ('Входные данные не удовлетворяют условию!')
