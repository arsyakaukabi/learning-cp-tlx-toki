s = list(map(int, input().split()))
print(('TIDAK', 'YA')[max(s) == sum(s)*4/7])
