n, m = map(int, input().split())
big = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    if big < min(tmp):
        big = min(tmp)
print(big)