n = int(input()); s = input()
ans = ''
for i in range(n-1):
    if s[i] != s[i+1]:
        ans += s[i]
print(ans+s[n-1])