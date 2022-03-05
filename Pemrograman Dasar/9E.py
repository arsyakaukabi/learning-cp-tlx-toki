I=lambda:list(map(int, input().split()))
n,m,p=I()
A = [I() for i in range(n)]
B = [I() for i in range(m)]
ans = [[sum(a*b for a,b in zip(Ar,Br)) for Br in zip(*B)] for Ar in A]
for r in ans: print(*r)