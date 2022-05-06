s='';f=False
for i in input():
    if i=='_':f=True
    elif f:s+=i.upper();f=False
    elif i.isupper():s+='_'+i.lower()
    else:s+=i
print(s)
