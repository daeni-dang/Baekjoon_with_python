N = int(input())
M = int(input())
S = input()

answer = 0
cnt = 0
i = 0
while i < M:
    if S[i:i+3] == "IOI":
        cnt += 1
        i += 2
    else:
        cnt = 0
        i += 1
    if cnt == N:
        answer += 1
        cnt -= 1

print(answer)