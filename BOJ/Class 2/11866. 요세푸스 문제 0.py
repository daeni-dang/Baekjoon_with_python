N, K = map(int, input().split())

arr = []
for i in range(N):
    arr.append(i + 1)
cnt = 0
idx = K - 1
answer = []
while cnt < N:
    answer.append(arr[idx])
    arr[idx] = 0
    Kcnt = 0
    while Kcnt < K:
        if cnt >= N - 1:
            break
        idx = (idx + 1) % N
        if arr[idx] != 0:
            Kcnt += 1
    cnt += 1
print("<"+', '.join(map(str, answer))+">")