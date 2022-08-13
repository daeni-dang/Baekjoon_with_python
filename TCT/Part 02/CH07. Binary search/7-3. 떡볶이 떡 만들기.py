n, m = map(int, input().split())
arr = list(map(int, input().split()))

height = 0
start = 0
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in arr:
        tmp = i - mid
        if tmp > 0:
            total += (i - mid)
    if total >= m:
        height = mid
        start = mid + 1
    elif total < m:
        end = mid - 1
print(height)