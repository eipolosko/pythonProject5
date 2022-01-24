n = input()
kol=0
kol=n.count('f')
print(kol)
if kol==1:
    print(n.index('f'))
elif kol>1:
    print(n.index('f'))
    print(n.rindex('f'))
if kol==0:
    print('NO')

a=list()
print(a)