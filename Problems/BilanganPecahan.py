import math; a, b = map(int, input().split())
x = math.gcd(a,b)
if x != 1: print(a//x,b//x)
else: print('Tidak')