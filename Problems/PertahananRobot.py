s = input(); _ = lambda x,j:x[j]-x[j+1]
a = [s.count(i) for i in 'RLUD']
print(_(a,0),_(a,2))