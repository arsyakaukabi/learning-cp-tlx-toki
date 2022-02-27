s = input()
a = [s.count(i) for i in 'RLUD']
print(a[0]-a[1],a[2]-a[3])