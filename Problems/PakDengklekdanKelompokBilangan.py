x = [int(input()) for _ in range(int(input()))]
p = []; n = []; z = []
for i in x:
    if i > 0: p+=[i]
    elif i < 0: n+=[i]
    else: z+=[i]
for i in (n+z+p):
    print(i)
