def binary_search_iter(arr, x):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        elif arr[mid] > x:
            end = mid - 1
    return None

def binary_search_recur(start, end, arr, x):
    mid = (start + end) // 2
    if start > end:
        return None
    if arr[mid] < x:
        return binary_search_recur(mid + 1, end, arr, x)
    elif arr[mid] > x:
        return binary_search_recur(start, mid - 1, arr, x)
    else:
        return mid

arr = list(map(int, input().split()))   # 주어진 배열
x = int(input())                # 찾으려는 숫자

# 1. 반복문 이용
result_iter = binary_search_iter(arr, x)
result_recur = binary_search_recur(0, len(arr) - 1, arr, x)
if result_iter == None or result_recur == None:
    print(-1)
else:
    print(result_iter)
    print(result_recur)