'''
    참고 : https://wooono.tistory.com/642
'''

import sys
input = sys.stdin.readline

def solution(n):
    dp = [[0] * 10 for _ in range(n + 1)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i - 1][j + 1]
            elif j <= 8:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
            else:
                dp[i][j] = dp[i - 1][j - 1]
    return sum(dp[n]) % 1000000000

def main():
    n = int(input())
    print(solution(n))

if __name__ == "__main__":
    main()