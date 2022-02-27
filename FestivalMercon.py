i = lambda:list(map(int, input().split()))
input(); a=i(); b=i()
print((0,1)[sum(a)%2])