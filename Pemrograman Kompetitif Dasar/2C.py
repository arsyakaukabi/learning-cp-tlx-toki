from math import gcd
D = [int(input()) for _ in range(int(input()))]
lcm = D[0]
for i in range(1, len(D)):
    lcm = lcm*D[i]//gcd(lcm, D[i])
print(lcm)
