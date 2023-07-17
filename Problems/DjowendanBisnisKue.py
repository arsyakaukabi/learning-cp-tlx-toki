from collections import Counter
I=input;I();print(sum(i%4 in{2,3}for i in Counter(I().split()).values()))
