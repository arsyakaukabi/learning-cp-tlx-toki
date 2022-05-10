I=input;s=[]
for _ in range(int(I())):
    b=I();s=sorted(s+[b])
    print(s.index(b)+1)