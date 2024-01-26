import sys
import math
input = sys.stdin.readline

def solution(n, k):
    return math.comb(n, k) % 10007
    # dp = [[0] * (n + 1) for _ in range(k + 1)]
    # for i in range(n + 1):
    #     dp[0][i] = 1
    # for i in range(1, k + 1):
    #     for j in range(i, n + 1):
    #         dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
    # return dp[k][n] % 10007

def main():
    n, k = map(int, input().split())
    print(solution(n, k))

if __name__ == "__main__":
    main()