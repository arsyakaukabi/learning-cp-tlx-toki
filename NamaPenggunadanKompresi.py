I=input;I();s=I()
print(''.join([s[i]for i in range(len(s)-1)if s[i]!=s[i+1]]+[s[-1]]))