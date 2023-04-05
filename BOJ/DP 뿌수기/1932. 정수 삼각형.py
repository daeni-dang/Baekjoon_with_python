n = int(input())
dp = [[0] * n for _ in range(n)]
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

dp[0][0] = tri[0][0]
for i in range(1, n):
    for j in range(len(tri[i])):
        if j - 1 >= 0:
            dp[i][j] = max(dp[i - 1][j - 1] + tri[i][j], dp[i - 1][j] + tri[i][j])
        else:
            dp[i][j] = dp[i - 1][j] + tri[i][j]

print(max(dp[-1]))