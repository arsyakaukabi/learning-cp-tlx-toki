s = input()
x = min([s.count(i) for i in 'bon'])
print((x-1, 0)[x == 0])
