n=int(input());a={}
for i in range(2,n+1):
    if n%i==0:
        c=0
        while n%i==0:
            n//=i
            c+=1
        a[i]=c