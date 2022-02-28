import math

def countLattice(r):
    if (r <= 0):
        return 0
    result = 4
    for x in range(1, r):
        ySquare = r*r - x*x
        y = int(math.sqrt(ySquare))
        if (y*y == ySquare):
            result += 4
    return result

n = int(input())
ans = -1
for i in range(1, n+1):
    if countLattice(i) == 12:
        ans = max(i, ans)
print(ans)
