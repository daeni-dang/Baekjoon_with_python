n = int(input())

dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(n):
    num = int(input())
    for j in range(4, num + 1):
        dp[j] = dp[j - 3] + dp[j - 2] + dp[j - 1]
    print(dp[num])