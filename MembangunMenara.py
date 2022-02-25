for _ in range(int(input())):
    L = []; H =[]
    for _ in range(int(input())):
        ABC = list(map(int, input().split()))
        L.append(min(ABC)); H.append(max(ABC))
    print(sum(L), sum(H))
