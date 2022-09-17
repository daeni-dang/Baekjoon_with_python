import sys

n, k = map(int, input().split())
coin = []
for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp <= k:
        coin.append(tmp)
coin_idx = len(coin) - 1
answer = 0
while k > 0:
    if k >= coin[coin_idx]:
        answer += k // coin[coin_idx]
        k %= coin[coin_idx]
    coin_idx -= 1
print(answer)