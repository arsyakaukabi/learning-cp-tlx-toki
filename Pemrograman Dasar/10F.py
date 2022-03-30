n,d=map(int,input().split());s=[list(map(int,input().split()))for _ in range(n)]
T={abs(s[i][0]-s[j][0])**d+abs(s[i][1]-s[j][1])**d for i in range(n)for j in range(n)if i!=j}
print(min(T),max(T))