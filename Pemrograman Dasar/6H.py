n, k = map(int, input().split())
for i in range(1, n+1):
    if i % k == 0:
        print('*', end=' ')
    else:
        print(i, end=' ')
