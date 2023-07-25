N = int(input())
arr = list(map(int, input().split()))
arr.sort()

cumsum = [arr[0]]
for i in range(1, N):
    cumsum.append(cumsum[i - 1] + arr[i])
print(sum(cumsum))