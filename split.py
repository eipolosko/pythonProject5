n = '1234 1234 1234 4321 4321 4321'
m = n.split()
m = '*'.join(m)
print(m)
l = n.split()
print(l)
k = n.split(',')
print(k)

n='hello'
n=n.split('l',2)
print(n)
t=[1,2,3,4,5]
t=''.join(str(i)for i in t)
print(t)

n = input()
n = ''.join(n.split())
print(n)
p=n[::-1]
if n==p:
    print('polindrom')
else:
    print('ne polindrom')

list = ["a", "b", "c"]
print(list)
print(*list) # работает только с print()
print(" ".join(list))
print(":".join(list))