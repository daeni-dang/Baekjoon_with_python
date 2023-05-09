import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    chapters = list(map(int, input().split()))
    cumsum = [0, chapters[0]]
    for i in range(1, K):
        cumsum.append(cumsum[-1] + chapters[i])

    dp = [[float("inf") for _ in range(K + 1)] for _ in range(K + 1)]
    for i in range(1, K + 1):
        dp[i][i] = 0
    for i in range(1, K + 1):
        for j in range(1, K + 1 - i):
            for k in range(j, i + j):
                dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + (cumsum[j + i] - cumsum[j - 1]))
    print(dp[1][-1])