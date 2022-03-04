from math import sqrt
for _ in range(int(input())):
    n = int(input())
    count = 0
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                count = 1
                break
        if count == 0:
            print("YA")
        else:
            print("BUKAN")
    else:
        print("BUKAN")
