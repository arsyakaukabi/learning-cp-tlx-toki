import statistics
input()
s = max(statistics.multimode(map(int, input().split())))
print(s)