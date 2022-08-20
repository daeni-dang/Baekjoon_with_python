n, m = map(int, input().split())

arr = list(map(int, input().split()))

ball = [0] * (m + 1)
for i in arr:
    ball[i] += 1

result = 0
for i in range(1, m + 1):
    n -= ball[i]
    result += ball[i] * n
print(result)