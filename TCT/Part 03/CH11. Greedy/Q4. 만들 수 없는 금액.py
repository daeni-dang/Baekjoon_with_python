n = int(input())

arr = list(map(int, input().split()))
arr.sort()

tmp = 1
for i in range(len(arr)):
    if arr[i] > tmp:
        break
    tmp += arr[i]
print(tmp)