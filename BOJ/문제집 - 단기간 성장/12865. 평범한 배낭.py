def solution(n, k, arr):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w = arr[i][0]
        v = arr[i][1]
        for j in range(1, k + 1):
            if j < w:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])
    return dp[-1][-1]

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = [[0, 0]]
    for i in range(n):
        arr.append(list(map(int, input().split())))
    print(solution(n, k, arr))
