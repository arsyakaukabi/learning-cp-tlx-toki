import sys
I=sys.stdin.readline().split()
n,d=int(I[0]),int(I[1])
s=[int(sys.stdin.readline()) for i in range(n)]
if d not in s:print(-1)
else:print(s.index(d))
