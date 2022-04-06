import fnmatch as fn
a=input();s=[input()for _ in range(int(input()))]
for i in s:print(i if fn.fnmatchcase(i,a) else '')
