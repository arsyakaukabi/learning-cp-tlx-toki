def f(i):
    j=i%10
    if j==0:return 0
    elif j==1:return 1
    elif j==2:x=[2, 4, 8, 6];return x[i%4-1]
    elif j==3:x=[3, 9, 7, 1];return x[i%4-1]
    elif j==4:x=[4, 6, 4, 6];return x[i%4-1]
    elif j==5:return 5
    elif j==6:return 6
    elif j==7:x=[7, 9, 3, 1];return x[i%4-1]
    elif j==8:x=[8, 4, 2, 6];return x[i%4-1]
    elif j==9:x=[9,1];return x[i%2-1]

for i in range(int(input())):
    n=int(input());ans=0
    for i in range(1,n+1):
        ans+=f(i)
        if ans>=10:
            ans%=10
    print(ans)