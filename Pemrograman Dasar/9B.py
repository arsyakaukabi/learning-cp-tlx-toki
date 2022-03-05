x = []
while True:
    try: x += [input()]
    except: break
for i in x[::-1]:
    print(i)