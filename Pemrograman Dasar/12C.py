a,b,k,x=map(int,input().split())
def f(x,k):
    if k==0:return x
    else:return abs(a*f(x,k-1)+b)
print(f(x,k))
