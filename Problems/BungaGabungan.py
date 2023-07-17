p, q = map(int, input().split())
x = (p*p+q*q+1)/4
print((-1, int(x))[x % 4 == 0])
