def binary_search(n_list, check):
    start = 0
    end = len(n_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if check == n_list[mid]:
            return "yes"
        elif check > n_list[mid]:
            start = mid + 1
        elif check < n_list[mid]:
            end = mid - 1
    return "no"

def counting(max_value, n_list, m_list):
    arr = [0] * (max_value + 1)
    for i in range(len(n_list)):
        arr[n_list[i]] = 1
    for i in m_list:
        if i > max_value:
            print("no", end=" ")
            continue
        if arr[i] == 1:
            print("yes", end=" ")
        else: print("no", end=" ")

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# 1. 이진 탐색 이용
n_list.sort()
for check in m_list:
    print(binary_search(n_list, check), end=" ")
print()

# 2. 계수 정렬 개념 이용
counting(max(n_list), n_list, m_list)