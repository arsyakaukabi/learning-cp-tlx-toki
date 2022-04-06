a,b=input(),input()
for i in range(len(a)):
    if a[:i]!=b[:i]:break
if a[i+1:]==b[i:]:print("Tentu saja bisa!")
else:print("Wah, tidak bisa :(")