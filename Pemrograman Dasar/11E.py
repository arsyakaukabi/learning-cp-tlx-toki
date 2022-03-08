def f(s):
    x = ''
    for i in s:
        if i.islower(): x += i.upper()
        else: x += i.lower()
    return x
print(f(input()))
