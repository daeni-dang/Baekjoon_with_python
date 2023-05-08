import sys
input = sys.stdin.readline

N = int(input())
m = [[0, 0]]
for i in range(N):
    m.append(list(map(int, input().split())))
dp = [[float("inf")] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    dp[i][i] = 0

for i in range(1, N + 1):
    for j in range(1, N + 1 - i):
        for k in range(j, N):
            dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + m[j][0] * m[k][1] * m[j + i][1])

print(dp[1][-1])