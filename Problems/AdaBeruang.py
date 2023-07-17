i = lambda:map(int, input().split())
N,D = i(); a = set(i())
s = {i+D for i in a}
print(len(a.intersection(s)))
