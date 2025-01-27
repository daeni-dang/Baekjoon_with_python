import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dp = [1, 2]
    for i in range(2, n):
        dp.append((dp[i - 2] + dp[i - 1]) % 15746)
    print(dp[n - 1])

if __name__ == "__main__":
    main()