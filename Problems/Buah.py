from math import gcd
_,a,b=map(int,input().split())
print(a//gcd(a,b)+b//gcd(a,b))