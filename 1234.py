a, b, c = int(input()), int(input()), int(input())
if a > b and b > c:
    print('max', a)
elif b > c:
    print('max',b)
else:
    print('max',c)

