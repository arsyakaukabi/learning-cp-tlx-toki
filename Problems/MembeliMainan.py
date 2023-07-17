x=int(input());k=0
a=sorted(map(int,input().split()))
while True:
    for i in a:
        if x>=i:x-=i;k+=1
        else:print(k);exit()