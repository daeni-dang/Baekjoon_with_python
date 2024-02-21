import sys
input = sys.stdin.readline

def solution(n, s):
    if n < 3:
        return sum(s)
    dp = [0] * n
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    dp[2] = max(s[0] + s[2], s[1] + s[2])
    if n == 3:
        return max(dp)
    for i in range(3, n):
        dp[i] = max(dp[i - 3] + s[i - 1], dp[i - 2]) + s[i]
    return dp[n - 1]

def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(int(input()))
    print(solution(n, s))

if __name__ == "__main__":
    main()