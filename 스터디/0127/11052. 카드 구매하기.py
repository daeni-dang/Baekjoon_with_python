import sys
input = sys.stdin.readline

def solution(n, cards):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = cards[0] * i
    for i in range(1, n + 1):
        for j in range(1, i // 2 + 1):
            if dp[i] < dp[j] + dp[i - j]:
                dp[i] = dp[j] + dp[i - j]
        if dp[i] < cards[i - 1]:
            dp[i] = cards[i - 1]
    return dp[n]

def main():
    n = int(input())
    cards = list(map(int, input().split()))
    print(solution(n, cards))

if __name__ == "__main__":
    main()