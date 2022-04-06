n=990000;s=[True]*n
for i in range(3,int(n**0.5)+1,2):
    if s[i]:s[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
l=[2]+[i for i in range(3,n,2) if s[i]]
for _ in range(int(input())):print(l[int(input())-1])