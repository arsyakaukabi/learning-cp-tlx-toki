n,m = map(int, input().split())
for i in range(n): print(('W'*m, 'B'*m)[i % 2])
