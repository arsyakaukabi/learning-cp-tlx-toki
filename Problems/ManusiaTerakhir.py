s=lambda k:0 if k<0 else 1
n,x,y=map(int,input().split())
x1,y1=[0,0],[0,0];p,q=abs(x),abs(y)
x1[s(x)],y1[s(y)]=p,q
if(p+q>n)|((n-p-q)%2==1):print(-1)
else:
    x1=[i+(n-p-q)//2 for i in x1]
    print(y1[1],x1[1],y1[0],x1[0])