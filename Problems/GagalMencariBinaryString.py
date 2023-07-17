_=input;n=int(_());s=''.join(i if i in'01'else''for i in _())
print((min(n-1,n-len(s.lstrip('0'))),-1)[len(s)==0])