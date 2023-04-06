n = int(input())

num = list(map(int, input().split()))

dp = [0] * n
dp[0] = num[0]
for i in range(1, n):
    dp[i] = max(num[i], num[i] + dp[i - 1])

print(max(dp))

'''
10 6 9 10 15 21 -14 12 33 32
'''