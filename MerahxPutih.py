from math import prod,sqrt
*x,=map(int,input().split());k=[0]*5
k[0]=sqrt(prod(x))/(x[1]*x[3])
for j in range(1,5):k[j]=x[j-1]/k[j-1]
print(' '.join([str(int(_)) for _ in k]))