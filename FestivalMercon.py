i=lambda:list(map(int,input().split()))
i();a=i();i()
print((0,1)[sum(a)%2])