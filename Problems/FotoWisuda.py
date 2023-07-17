for _ in range(int(input())):
    M=0;p=set()
    for _ in range(int(input())):
        s=input().split(' ')
        p|=set(s[2:])
        if s[0][0]=='d':M=max(M,int(s[1]))
    print((len(p),len(p)+1)[len(p)==M])