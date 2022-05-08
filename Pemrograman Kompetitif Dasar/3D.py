from bisect import bisect as II
I=lambda:list(map(int,input().split()))
I();*s,=I()
for _ in range(int(input())):
  x,y=I();print(II(s,y)-II(s,x))