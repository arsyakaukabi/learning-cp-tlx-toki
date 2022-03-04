for i in range(1, int(input())+1):
    if i == 42:
        print('ERROR')
        exit()
    elif i % 10 != 0:
        print(i)
