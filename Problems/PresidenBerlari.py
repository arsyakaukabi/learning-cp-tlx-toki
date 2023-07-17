n, k = map(int, input().split())
print((k*2**(n-k),n)[n<k])