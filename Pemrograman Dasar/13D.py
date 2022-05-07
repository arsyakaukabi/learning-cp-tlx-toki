from itertools import permutations as i1
from sys import stdout as i2
n=int(input())
for x in i1([_ for _ in range(1,n+1)]):
    f=True
    for i in range(1,n-1):
        if(x[i]<x[i-1])!=(x[i]<x[i+1]):f=False
    if f:i2.write(''.join(map(str,x))+'\n')