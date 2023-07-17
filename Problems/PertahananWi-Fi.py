k = lambda: map(int, input().split())
n, m = k(); s = sorted(k())
ans = max(s)-min(s)
for i in range(n-m+1):
    ans = min(ans,s[i+m-1]-s[i])
print(ans)
