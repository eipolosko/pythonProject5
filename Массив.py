# el=list()
# print(el)
# el = [1,3,3,4,'f',2]
# print(el)
# el.insert(0,111) #куда вставить,сам элемент
# el[0]=2222#изменение элемента
# print(el)
#
# #заполнение списка рандомными элементами
# import random
# c=[random.randint(0,100) for i in range(10)]
# print(c)
# print(c[0])
# print(c[-1])
# print(c[5])
# print(c[-4])

#удаление
el = [1,3,3,4,'f',2,'f']
del el[1] #удаление по индексу
el.remove('f')# по значению
el.remove('f')
print(el)
#вложенные списки удаление
my_list = ['hello','world']
elements = [1,3,my_list,6,'a','b']
del elements[2][1] #первое номер в elements,второе в mylist

el = [1,3,6,'a','b','abc',123,435]
del el[4:] #удаляем после четвертого
print(el)
del el[:2]#удаляем до 2
print(el)
del el[1:3]#удаляем с 1 до 3
print(el)

#поиск
el = [1,3,6,'a','b','abc',123,435]
if 'abc'in el:
    print("yes")

#объединение
a =[1,3,5]
b = [1,3,5,7]
print(a+b)

d=['h','e','l','l','o']
e = ['w','o','r','l','d']
d.extend(e)
print(d)

#копирование 1 способ
a=['кот','слон','змея']
b=a.copy()
print(a,b)
#копирование 2 способ
d=list(a)
print(a,d)
#копирование 3 способ
import copy
e=copy.copy(a)
print(a,e)
#копирование 4 способ
t=copy.deepcopy(a)
print(a,t)

#срезы
m=[1,2,3,4,5,6,7,8]
n = m[0:8:2]
print(m,n)

#перебор элементов for
a=[1,2,3,'neon']
for i in a:
    print(i)

#перебор элементов while
a=[1,2,3,'neon']
s=len(a)
i=0
while i<s:
    print(a[i])
    i+=1

a=[1,2,3]
b=a.copy()
print(id(a),id(b),a,b)

#pop
el=[1,'weow',3,'weow']
m=el.pop(1)#возвращает удаленный элемент
print(m)
print(el)
#в обратном порядке
el.reverse()
print(el)
#сортировка
a =[3,22,4,1,3,4,6,7]
a.sort() #по возрастанию
print(a)
a.sort(reverse=True)#по убыванию
print(a)

