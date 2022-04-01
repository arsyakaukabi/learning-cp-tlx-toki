I=lambda:list(map(int,input().split()))
n,r,v=I();w=[abs(i-v)for i in I()]
print(-1 if min(w)==0 else r/min(w))