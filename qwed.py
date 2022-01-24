import random
ar = []
n = int(input())
k=0
#q=0
for i in range(n):
    new = int(input())
    ar.append(new)
#for i in range (0,n+1):
   # k += ar[i]
    #if ar[i]==0:
      # break
for i in range (n):
    per=ar.index(0)
    vt = ar.index(0, per + 1, n)


print(per)
print(vt)

# print(ar)
# print(per)
# print(vt)




