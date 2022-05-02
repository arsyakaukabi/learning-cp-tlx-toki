n=int(input());a={}
for i in range(2,n+1):
    if n%i==0:
        c=0
        while n%i==0:n//=i;c+=1
        a[i]=c

x=[(k,v) for k,v in a.items()]
for j in range(len(x)):
    print(x[j][0],end='')
    if x[j][1]!=1:print('^'+str(x[j][1]),end='')
    if j!=len(x)-1:print(' x ',end='')
