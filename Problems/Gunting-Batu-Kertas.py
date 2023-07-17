i=input;i();s1=i();s2=i()
g1,b1,k1=[s1.count(i) for i in 'GBK']
g2,b2,k2=[s2.count(i) for i in 'GBK']
print(min(g1,k2)+min(b1,g2)+min(k1,b2))