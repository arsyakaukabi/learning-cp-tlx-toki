input();s=[input().split() for _ in range(2)]
for i in range(int(input())):
    p,x,q,y=[int(i)-1 if i.isdigit() else ord(i)-65 for i in input().split()]
    s[p][x],s[q][y]=s[q][y],s[p][x]
for _ in s:print(*_)