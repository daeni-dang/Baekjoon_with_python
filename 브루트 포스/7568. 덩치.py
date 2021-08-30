dung = []
n = int(input())
rank = [1] * n
for i in range(n):
    x, y = map(int, input().split())
    dung.append([x, y])
for i in range(n):
    rank = 1
    for j in range(n):
        if i == j: continue
        if dung[i][0] < dung[j][0] and dung[i][1] < dung[j][1]:
            rank += 1
    print(rank, end=' ')