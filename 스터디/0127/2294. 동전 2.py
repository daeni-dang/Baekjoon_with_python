import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    coins = []
    dp = [1e9] * (k + 1)
    for _ in range(n):
        coins.append(int(input()))
        if coins[-1] <= k:
            dp[coins[-1]] = 1
    for i in range(2, k + 1):
        for j in range(n):
            # if i - coins[j] > 0:
            dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    print(dp[-1] if dp[-1] != 1e9 else -1)

if __name__ == "__main__":
    main()