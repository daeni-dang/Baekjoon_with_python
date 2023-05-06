import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
nums = [0] + list(map(int, input().split()))
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][i] = 1
    if i + 1 <= N and nums[i] == nums[i + 1]:
        dp[i][i + 1] = 1

for i in range(2, N + 1):
    for j in range(1, N + 1 - i):
        if nums[j] == nums[j + i]:
            dp[j][j + i] = dp[j + 1][j + i - 1]
   
M = int(input())
for i in range(M):
    flag = 1
    S, E = map(int, input().split())
    print(str(dp[S][E]) + "\n")
    