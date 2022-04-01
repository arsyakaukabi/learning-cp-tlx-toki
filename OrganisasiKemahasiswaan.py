I=lambda:map(int,input().split())
for _ in range(int(input())):
    n,k=I();*m,=I()
    print(max(max(m),-(-sum(m)//k)))