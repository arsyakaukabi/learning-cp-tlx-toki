x = int(input())
i = 2
f1 = 0; f2 = 1
while x > f2:
    f3 = f1+f2
    f1 = f2
    f2 = f3
    i += 1
print(i if x == f3 else 0)
