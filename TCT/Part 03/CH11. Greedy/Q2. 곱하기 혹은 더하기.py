s = input()
answer = 0

for i in range(len(s)):
    if s[i] <= '1' or answer <= 1:
        answer += int(s[i])
    else:
        answer *= int(s[i])
        
print(answer)