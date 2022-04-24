n=int(input())
*a,=set(map(int,input().split()))
p=1
if len(a)!=n:print(0)
else:
    for i in range(n):
        for j in range(i+1,n):
            p=p*(a[i]^a[j])%998244353
    print(p)