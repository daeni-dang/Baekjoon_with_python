n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))

'''
dp[i] = i번째까지 최대 점수
'''
if n < 3:
    print(sum(s))
elif n == 3:
    print(max(s[0] + s[2], s[1] + s[2]))
else:
    dp = [0] * n
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    dp[2] = max(s[0] + s[2], s[1] + s[2])
    for i in range(3, n):
        dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
    print(dp[-1])