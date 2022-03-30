for _ in range(int(input())):
    c=0;n=int(input())
    for i in range(1,int((n**0.5)+1)):
        if n%i==0:c+=1
    print(('BUKAN','YA')[c<=2])