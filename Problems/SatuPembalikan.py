n = int(input()); i = lambda:list(map(int,input().split()))
a = i(); b = i(); c = 0
for i in range(n):
    if a[i] == b[i]:
        c += 1
print(c)