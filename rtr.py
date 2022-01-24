list = [76,1,23, 48, 'hello', 6, 19, 'world']
print('Числа из списка')
for i in list:
    i=str(i)
    if i.isdigit() == True:
       sum=0
       if int(i)%2==0:
           print(f'{i} - четное')
           for a in i:
               sum+=int(a)
           print(f'Сумма цифр числа {i} равна {sum}')
       else:
           print(f'{i} - нечетное')

           ind=list.index(int(i))
           list[ind]=1

print('Измененный список (нечетные числа заменены на единицу')
print(list)
print('-----------------------------')
print('Слова из списка')
for i in list:
    i=str(i)

    if i.isalpha()==True:
        print('*************************')
        print(i)
        kol = 0
        kol1 = 0
        for m in i:
            if m in 'eyuioa':
                print(f'{m} гласная')
                kol+=1
            else:
                print(f'{m} согласная')
                kol1+=1
        print(f'Количество гласных  {kol}\n Количество согласных {kol1}')

