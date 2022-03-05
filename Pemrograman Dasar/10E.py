a,b,k,x=map(int,input().split())
f = abs(a*x+b)
for i in range(k-1):
    f = abs(a*f+b)
print(f)