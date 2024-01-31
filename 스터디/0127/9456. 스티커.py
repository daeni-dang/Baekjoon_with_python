import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        stickers = []
        for _ in range(2):
            stickers.append(list(map(int, input().split())))
        if n == 1:
            print(max(stickers[0][0], stickers[1][0]))
            continue
        dp = [[0] * n for _ in range(2)]
        for i in range(2):
            dp[i][0] = stickers[i][0]
        for i in range(2):
            dp[i][1] = max(stickers[i][1], stickers[(i + 1) % 2][0] + stickers[i][1])
        for j in range(2, n):
            for i in range(2):
                dp[i][j] = max(dp[i][j], max(dp[(i + 1) % 2][j - 2], dp[(i + 1) % 2][j - 1]) + stickers[i][j])
        print(max(dp[0][n - 1], dp[1][n - 1]))

if __name__ == "__main__":
    main()