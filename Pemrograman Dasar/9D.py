I = lambda: list(map(int, input().split()))
n, m = I()
a = []
for i in range(n):
    a.insert(i, I())
x = [[a[i][j] for i in range(n)][::-1] for j in range(m)]
for i in range(m):
    print(*x[i])
