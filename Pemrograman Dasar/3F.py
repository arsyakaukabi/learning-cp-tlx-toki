A = []
for i in range(3):
    A += [input().split()]
T = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
for j in T:
    print(*j, sep=" ")
