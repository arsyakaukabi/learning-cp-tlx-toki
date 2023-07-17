n,m=map(int,input().split())
s=[[0]*m for _ in range(n)]
for i in range(1,1+n):
    for j in range(1,1+m):
        if i%2==0 and j%2==0:s[i-1][j-1]='#'
        elif i%2!=0 and j%2!=0:s[i-1][j-1]='*'
        else:s[i-1][j-1]='$'
for i in s:print(''.join(i))