I=lambda:map(int,input().split())
n,m=I();a,b=I()
print(max((n//a)*(m//b),(n//b)*(m//a)))