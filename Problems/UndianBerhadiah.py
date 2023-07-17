n,x=map(int,input().split());m=1e6
for _ in range(n):
    y=int(input());d=abs(y-x)
    if m>d:m=d;v=[y]
    elif d==m:v+=[y]
for i in sorted(v):print(str(i).zfill(5))
# Hati-hati dengan leading zeros, pastikan 5 digit.