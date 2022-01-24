n=int(input())
m=int(input())
for i in range(n+1):
    for j in range (m+1):
        if i==0 and j==0 or i==n and  j==m:
            print(n*'*')
        else:
            if 0<i<n-1 and j==0:
                print('*','*',sep=(n-2)*' ')
