a,b,m=map(int,input().split())
c={a,b};f1=a;f2=b
while True:
    f3=(f1+f2)%m
    f1=f2
    f2=f3
    c.add(f3)
    if f1==a and f2==b:
        print(len(c))
        exit()