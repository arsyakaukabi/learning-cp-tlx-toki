from bisect import bisect
from itertools import accumulate
I=lambda:list(map(int,input().split()))
I();*a,=accumulate(I());b=I()
for x in b:print(bisect(a,x))