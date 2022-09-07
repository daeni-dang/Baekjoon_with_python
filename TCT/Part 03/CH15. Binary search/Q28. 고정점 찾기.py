n = int(input())

arr = list(map(int, input().split()))

start = 0
end = n - 1
flag = False

while start <= end:
    mid = (start + end) // 2
    if mid == arr[mid]:
        print(mid)
        flag = True
        break
    if arr[mid] > mid:
        end = mid - 1
    else:
        start = mid + 1
        
if not flag:
    print(-1)