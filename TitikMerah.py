I=lambda:map(int,input().split())
n,r,v=I();w=min([abs(i-v)for i in I()])
print(-1 if w==0 else r/w)