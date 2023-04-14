# dp[i] = max(dp[i - 1], dp[i - 2]) + dp[i]

n = int(input())
stairs = []
for i in range(n):
    stairs.append(int(input()))

dp = [0] * n
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n - 1])

'''
1 -> 1
2 -> 1+2
3 -> 1+3 / 2+3
4 -> 1+2+4 / 1+3+4 / 2+4
5 -> 1+2+4+5 / 
'''