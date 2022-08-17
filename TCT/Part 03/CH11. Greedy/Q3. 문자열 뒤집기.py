s = input()

result = [0] * 2

if s[0] == '1':
    result[0] += 1
else:
    result[1] += 1
    
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == '1':
            result[0] += 1
        else:
            result[1] += 1
print(min(result))