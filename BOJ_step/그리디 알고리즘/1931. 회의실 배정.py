import sys
n = int(input())
meeting = []
for i in range(n):
    meeting.append(list(map(int, sys.stdin.readline().split())))
meeting.sort(key=lambda x : (x[1], x[0]))
answer = 1
end_time = meeting[0][1]
for i in range(1, n):
    if meeting[i][0] >= end_time:
        end_time = meeting[i][1]
        answer += 1
print(answer)