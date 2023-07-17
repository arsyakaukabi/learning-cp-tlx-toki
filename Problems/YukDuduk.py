n=int(input());s=[input()for _ in range(n)]
for j in range(n//2):print(s[j]);print(s[-(j+1)])
if n%2:print(s[n//2])
