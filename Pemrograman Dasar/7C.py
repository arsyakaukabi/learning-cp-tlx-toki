n = int(input())
r = 0
for i in range(1, n+1):
    for j in range(i):
        print(r, end='')
        r += 1
        if r == 10:
            r = 0
    print(end='\n')
