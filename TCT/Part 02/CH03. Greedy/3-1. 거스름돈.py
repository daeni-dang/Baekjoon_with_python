n = int(input())
coin = [500, 100, 50, 10]
coin_idx = 0
answer = 0

for c in coin:
    answer += n // c
    n %= c

print(answer)