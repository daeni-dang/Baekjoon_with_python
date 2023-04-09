n = int(input())

dp = [0] * 1001
dp[1], dp[2] = 1, 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])

'''
2x1 -> 1
2x2 -> 2
2x3 -> 3
2x4 -> 5
2x5 -> 8
2x6 -> 13
2x7 -> 21
2x8 -> 34
2x9 -> 55
'''