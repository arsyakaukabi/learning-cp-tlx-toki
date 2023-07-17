n=int(input())+2980232238769531;f=0
while n:
    n,r=divmod(n,5)
    if r>2:f=1
print('YNEOS'[f::2])