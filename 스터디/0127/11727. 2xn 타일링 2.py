import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dp = [1, 3]
    for i in range(2, n):
        dp.append((dp[i - 2] * 2 + dp[i - 1]) % 10007)
    print(dp[n - 1])

if __name__ == "__main__":
    main()