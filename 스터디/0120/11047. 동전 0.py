import sys
input = sys.stdin.readline

def main():
    answer = 0
    N, K = map(int, input().split())
    coins = []
    for _ in range(N):
        coin = int(input())
        if coin <= K:
            coins.append(coin)
    for coin in reversed(coins):
        answer += K // coin
        K -= K // coin * coin
    print(answer)

if __name__ == "__main__":
    main()