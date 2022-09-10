have = list(map(int, input().split()))
need = [1, 1, 2, 2, 2, 8]
result = []

for i in range(len(have)):
    result.append(need[i] - have[i])

for i in result:
    print(i, end=' ')