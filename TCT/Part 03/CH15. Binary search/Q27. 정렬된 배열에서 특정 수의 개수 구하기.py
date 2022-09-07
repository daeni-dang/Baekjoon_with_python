n, x = map(int, input().split())

arr = list(map(int, input().split()))

def binary_left():
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > x:
            start = mid + 1
        elif arr[mid] < x:
            end = mid - 1
        else:
            if mid >= 1 and arr[mid - 1] != x:
                return mid
            else:
                mid -= 1
        print(mid)
    return None
            
def binary_right():
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        print(mid)
        if arr[mid] > x:
            start = mid + 1
        elif arr[mid] < x:
            end = mid - 1
        else:
            if mid < n and arr[mid + 1] != x:
                return mid
            else:
                mid += 1
                
print(binary_right() - binary_left())