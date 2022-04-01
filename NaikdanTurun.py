n,q=map(int,input().split())
L,R=0,0
for i in range(q):
    t,x,y=map(int,input().split())
    if t==1:
        L+=y
        if x==n:
            R+=y
    else:
        R-=y
        if x==n:
            L-=y
print(max(abs(L),abs(R)))