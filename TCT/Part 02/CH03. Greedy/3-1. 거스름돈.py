n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

answer = ((m - (m // (k + 1))) * arr[0]) + ((m // (k + 1)) * arr[1])
print(answer)