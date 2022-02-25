word = 'halo dunia'
char = input().lower()
count = 0
for i in range(min(len(word), len(char))):
    if char[i] == word[i]:
        count += 1
print(count)
