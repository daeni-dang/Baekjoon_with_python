import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dp = [1, 1]
    for i in range(2, n):
        dp.append(dp[i - 2] + dp[i - 1])
    print(dp[-1])

if __name__ == "__main__":
    main()