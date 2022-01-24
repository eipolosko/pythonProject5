import random
k=0
q = random.randint(1, 10)
w = random.randint(1, 2)
while k<5:
    n = int(input('введите число от 1 до 10\n'))
    m = input('введите красный или черный\n')

    k+=1
    if w==1:
        a='красный'
    if w==2:
        a='черный'
    if q==n and a==m:
        print('вы угадали число и цвет', q,a)
    else:
        print('попробуйте еще раз. правильный ответ-', q,a)


